# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
#
|            | App service                                                                         | VM       |Note|
|------------|-------------------------------------------------------------------------------------|----------| ---|
|Cost        | Database: Basic tier 4.9 USD/month for 2GB storage. App service: F1 tier 0 USD/month|Standard_B1s: 10.66 USD/month 1 GiB memory, 1vcpu|Project 1 is a lightweight Python application with a very simple database and logging service. These plans will be the most suitable for deploying Project 1. Based on the cost of the app service and VM column, we can see the app service is a suitable choice with a lower cost.    | 
|Scalability | Maximum hardware capability: 14GB of memory and 4 vCPU cores per instance      | Recommendation VM for general purposes can be up to 4vCPU, 32 GiB RAM, 28 GiB temp storage (DS3_v2). HDD, SSD disk size up to 32 TB. Blob Storage | Both the app service and the VM are scalable. Azure has many options for VMs with a higher price and greater capability, and it depends on the location that we choose. As we can see, the resource of an app service can easily adapt Project 1's application. Otherwise, we don't need too much focus on the infrastructure for this application. The app service helps us deploy Project 1 easily and with less effort.    |
|Availability| High availability   | High availability        |Azure users can control the availability of VMs with availability zones. But this application doesn't really need this benefit. The availability of the VM and app services has been guaranteed by Microsoft.    |
|Workflow    | CI/CD with source control (Github, Azure Repository, Bitbucket, Local git repository). Manual deployment (FTP)  | CI/CD with source control (Azure repository). Manual deployment        | Based on document from Microsoft, both App service and VM can support CI/CD. https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/cicd-for-azure-vms   |


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 