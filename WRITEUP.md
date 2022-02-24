# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*

APP SERVICE: The costs, scalability, and availability for a CMS app deployed through an App Service are reasonable and even free on lower tiers. This is a fairly small app with little to no traffic, so it does not need a alot of compute capability.

Even though the service plans are constant and the user is paying even when no one is accessing the service, the reduced compute requirements of a CMS app are not expensive.

Continous deployment through GitHub workflows on the Azure portal makes updating the CMS app quick and easy with github pushes and pulls being the most complex part so it's no issue at all.

VM: The costs, scalability, and availability for a CMS app deployed through a VM are like t he app service quite cheap and we do have a pay as you use availability thats not just a flat fee with no consumption.

The VM allows for more customization of the app's capability, though we don't really need that level of customizability in this current project, but if we did need to take control of those bits we would definitely look into this more if we wanted to finetune the whole VM just for our CMS.


My Choice: I chose App Service because the CMS app is lightweight, does not require robust compute power, and is easy to deploy through Azure.

### Assess app changes that would change your decision.
If i needed more robust compute power, higher security levels (i.e. I wanted to control more aspects of where the app sits), or I would start to consider the VM instead. 



