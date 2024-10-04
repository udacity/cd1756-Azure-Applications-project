"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for
from werkzeug.urls import url_parse
from config import Config
from FlaskWebProject import app, db
from FlaskWebProject.forms import LoginForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from FlaskWebProject.models import User, Post
import msal
import uuid

imageSourceUrl = 'https://'+ app.config['BLOB_ACCOUNT']  + '.blob.core.windows.net/' + app.config['BLOB_CONTAINER']  + '/'

@app.route('/')
@app.route('/home')
@login_required
def home():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    posts = Post.query.all()
    return render_template(
        'index.html',
        title='Home Page',
        posts=posts
    )

@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post()
        post.save_changes(form, request.files['image_path'], current_user.id, new=True)
        return redirect(url_for('home'))
    return render_template(
        'post.html',
        title='Create Post',
        imageSource=imageSourceUrl,
        form=form
    )


@app.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def post(id):
    post = Post.query.get(int(id))
    if request.args.get('action')=='delete':
        # if the post has image also, delete it
        if post.image_path != None:
            post.delete_image()
        db.session.delete(post)
        db.session.commit()
        flash(f'post "{post.title}" deleted successfully')
        return redirect(url_for('home'))
    form = PostForm(formdata=request.form, obj=post)
    if form.validate_on_submit():
        post.save_changes(form, request.files['image_path'], current_user.id)
        return redirect(url_for('home'))
    return render_template(
        'post.html',
        title='Edit Post',
        imageSource=imageSourceUrl,
        form=form
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password_hash == '-': 
            # OAuth2 users are not allowed to use password
            flash('Not Allowed! Sign in with your Microsoft Account')
            return redirect(url_for('login'))
        elif user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            # Log for unsuccessful login attempt:
            app.logger.warning("Invalid login attempt!")
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        # Log for successful login:
        app.logger.warning(f"{user.username} logged in successfully")
        flash(f'Welcome {user.username} !')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    session["state"] = str(uuid.uuid4())
    auth_url = _build_auth_url(scopes=Config.SCOPE, state=session["state"])
    return render_template('login.html', title='Sign In', form=form, auth_url=auth_url)

@app.route(Config.REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
def authorized():
    if request.args.get('state') != session.get("state"):
        return redirect(url_for("home"))  # No-OP. Goes back to Index page
    if "error" in request.args:  # Authentication/Authorization failure
        return render_template("auth_error.html", result=request.args)
    if request.args.get('code'):
        cache = _load_cache()
        # TODO: Acquire a token from a built msal app, along with the appropriate redirect URI
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
            code=request.args['code'],
            scopes=Config.SCOPE,
            redirect_uri=url_for('authorized', _external=True, _scheme="https"))
        session["user"] = result.get("id_token_claims")
        # Get user name from result, preferred_username is email
        username = session["user"].get('preferred_username').split('@')[0] # Preprocess the email and use it for username
        user = User.query.filter_by(username=username).first()
        if not user:
            new_user = User(username=username,password_hash='-')
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(username=username).first()
        login_user(user)
        flash(f'Welcome {user.username} !')
        _save_cache(cache)
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    logout_user()
    if session.get("user"): # Used MS Login
        # Wipe out user and its token cache from session
        session.clear()
        # Also logout from your tenant's web session
        return redirect(
            Config.AUTHORITY + "/oauth2/v2.0/logout" +
            "?post_logout_redirect_uri=" + url_for("login", _external=True, _scheme="https"))

    return redirect(url_for('login'))

def _load_cache():
    # TODO: Load the cache from `msal`, if it exists
    cache = None
    return cache

def _load_cache():
    # TODO: Load the cache from `msal`, if it exists
    cache = msal.SerializableTokenCache()
    token_cache = session.get('token_cache')
    if token_cache:
        cache.deserialize(token_cache)
    return cache

def _save_cache(cache):
    # TODO: Save the cache, if it has changed
    if cache.has_state_changed:
        session['token_cache'] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    # TODO: Return a ConfidentialClientApplication
    return msal.ConfidentialClientApplication(
        authority=authority or Config.AUTHORITY,
        client_id=Config.CLIENT_ID,
        client_credential=Config.CLIENT_SECRET,
        token_cache=cache)

def _build_auth_url(authority=None, scopes=None, state=None):
    # TODO: Return the full Auth Request URL with appropriate Redirect URI
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes=scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri=url_for('authorized', _external=True, _scheme='https')
        )
