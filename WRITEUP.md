# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Analysis of VM
- Cost:             More expensive option
- Scalability:      Multiple VM's needed for scalability
- Availablity:      Multiple VM's needed for high availability
- Workflow:         More work involved to set up and maintain a VM. 

### Analysis of App Service
- Cost:             less expensive option
- Scalability:      Auto-scaling
- Availablity:      Has high availability
- Workflow:         Low maintenance, only responsible for the application itself.

Overall, the App Service would be the better option. It is lower cost, has built in scalability and availability versus (VM
which requires multiple instances) and is an easier workflow for a simple web application. Since our web app is Flask and
is only dependent on Python, we don't require the flexibility to modify OS or install extra software.


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

A few reasons why we might need to use VM's over App Service are if we need control of the underlying OS or need to install
software on the server. If we knew precisely how much availability we needed a VM would be the better option because we could
turn it off when not in use as opposed to App Service which is always running and charging you for the service.
