## Compare Azure VM and App Service

### Analyze costs

**Microsoft Azure Virtual Machines** are generally more flexible but can be more expensive, with costs starting around **$0.096 per hour** for the VM itself, plus additional costs for storage and networking. 

**Azure App Services**, on the other hand, are a Platform-as-a-Service (PaaS) offering optimized for web apps like Flask, with pricing starting at **$9.49 per month** for the Basic tier. App Services can be more cost-effective for web applications due to their managed nature and scalability options.


### Analyze scalability

**Azure Virtual Machines (VMs)** offer scalability by allowing to manually scale up (increase resources like CPU, memory, etc.) or scale out (add more VM instances). We can also use **Virtual Machine Scale Sets** to automatically increase or decrease the number of VM instances based on demand.

**Azure App Services**, on the other hand, provide built-in **automatic scaling**. This feature allows our app to automatically adjust the number of instances based on incoming traffic, ensuring that our app can handle varying loads without manual intervention.


### Analyze availability

**Azure Virtual Machines (VMs)** offer high availability through features like **Availability Sets, Availability Zones**, and **Virtual Machine Scale Sets**. These options help ensure that our VMs remain operational even during hardware failures or maintenance events.

**Azure App Services** also provide high availability by supporting **multi-region deployments** and **availability zones**. This means our web app can automatically distribute across different zones and regions to minimize downtime and ensure continuous operation.


### Analyze workflow

**Azure Virtual Machines (VMs)** require a more hands-on approach to workflow management. We need to manually set up the VM, configure the operating system, install necessary software, and manage updates and maintenance ourselves. Automation tools like **Azure Automation, Terraform**, and **Ansible** can help streamline these tasks.

**Azure App Services**, on the other hand, offer a more streamlined workflow. We can deploy your Flask app directly from the Azure portal, GitHub, or other CI/CD tools like **GitHub Actions**. The platform handles much of the underlying infrastructure management, allowing you to focus more on our application code.


## Chosen Azure Service and justification

For a Flask app, I would choose **Azure App Services**. It provides a streamlined deployment process, automatic scaling, and managed infrastructure, which allows me to focus more on developing my app rather than managing servers. Plus, it's typically more cost-effective for web applications compared to the flexibility of Virtual Machines. In short, it is better fit for purpose as I see it.


## Assess app changes that would change your decision

### How will the app change per your decision, such as the application requirement or more control over the infrastructure?

If the application changes in a way that requires more control over the infrastructure, such as needing custom configurations, running multiple services, or installing specific software, then **Azure Virtual Machines (VMs)** would be a better choice. VMs provide greater flexibility and control over the operating system and environment, allowing for tailored setups that might not be possible with the more managed Azure App Services.

On the other hand, if the app scales significantly and requires high availability, frequent updates, and automated deployments, sticking with **Azure App Services** would be beneficial due to its ease of use and robust scaling capabilities.


### List any other needs you must change to suit your application requirements?

To suit my application requirements, I might need to switch to NoSQL CosmosDB database, set up CI/CD pipelines, and ensure high performance with caching. Additionally, implementing auto-scaling and security measures would help to maintain reliability and protection.
