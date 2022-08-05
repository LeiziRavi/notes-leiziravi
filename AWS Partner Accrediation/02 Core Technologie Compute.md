- Compute services allow customers to 
	- __develop, deploy, run and scale workloads in aws cloud.
	- Some of these products:
		- __Amazon ElasticCompute2__ : Resizable compute capacity
			- Compute capacity refers to the capacity that traditionally refers to functionality that is traditionally provided by on-primise pysical  or virtual servers
			- Offers broadest and deepest compute platform
			- WIth over 400 instances and choice of processors , storage, networking and os and purchased model.
		- __Amazon EC2 Auto Scaling__: Increase or decrease number of instances
			- With autoscaling customers can maintain health and availability to their applciations by setting triggers to automatically increase and decrease the number of instances in their deployments.
		- __Elastic Load Balancing__: Distributing incoming traffic
			- Automatically distributes incoming traffic across multiple targets such as amazon EC2 instances, containers, ipaddresses, and lambda functions.
		- __Amazon Elastic Container Service__: Run applications on a managed cluster
			- Highly scalable, high performance container management services that supports docker containers and allows customers to easily run applications on a managed cluster of Amazon EC2 insatnces or an AWS farGate.
			- AWS FarGate is a serverless, pay-as-u-go compute engine that is complatible with both elastic container service and amazon kubernetes service.
		- __Amazon Elastic Kubernetes Service__: Run Kubernetes applications on AWS and on-permoses
			- Automatically manages the availablity and scalability of the kubernetes control plane node responsible for scheduling containers, managing application availability, storing cluster data and other key tasks.
		- __AWS Lambda__: Run code in response to events
			- runs code without the need to provision or manage servers.
			- It is referred to as serverless computing.
			- starts  running code in miliseconds of an event, such as image upload, in-app activity, website click, or output from an connected device



#### Benefits of Amazon EC2:
- __Elasticity__: Enables customers to increase or decrease compute capacity with minutes not hours and days.
	- Combined wIth Customers Amazon EC2 auto scaling, customers maintain availability of there EC2 fleet and automatically scale up and down depending on theie needs in order to maximise performance and minimize cost.
- __Control__:
	- Customers have complete control of their instances, including root/administrator access and the ability to interact with it as they would with any machine.
- __Flexibility__: Flexible cloud hosting service
	- Customers have choice of multiple instance types, operating systems and software packages.
- __Integrated__: 
	- Amazon EC2 is integarted with most of the aws services, to provide, complete and secure solution for computing query processing and cloud storage across a wide range of applications.
- __Reliable__:
	- provides highly relaible environment where replacement instances can be rapidly and predictably commissioned.
	- The service run within amazons proven network infrastructure and data centres. 
- __Secure__:
	- aws customers benefit from a datacenter and a network architecture build to meet the needs of the most security sensitive organisations. 
- __Cost-effective__: 
	- Using amazon EC2, let's customers take advantage of amazon scale. 
	- It enables customers to pay a very low rate to compute capacity they actually consume.
- __Easy__:
	- aws is free to get started.
	- Customers can leverage the management console, the cli or the sdks.



#### Amazon EC2 choices : Instance Types
- It provides wide of selection of hardware and software configurations optimized to fit different use cases.
- Instance types comprise varying combination of CPU, memory, storage and networking capacity to give the flexibility to choose the appropriate mix of resources to our applications.
- Intances are first divided into several general categories, 
	- __General Purpose__ instance provides balance of compute, memory and network resources and can be used for variety of diverse workloads.
	- __Compute Optimized__ instances are ideal for compute bound applciations that benefit from high performance processor.
	- Memory Optimized instances are designed to deliver fast performance for workloads that process large data sets to memory.
	- Accelerated Computing instances use hardware accelerators or co-processors to perform functions such as floating point calculations, graphics processing, data pattern matching, more efficiently thn is possible by softwares running on CPUs. 
	- Storage Optimized instances are designed for workloads that require high sequential read and write access to very large data sets on local storage. They are optimized to deliver tens of thousands of low latency, random io operations per second or iops to operations.

- Each category has different family with fundamental differences within the category. for instance general purpose category has four families, Mac, A, T and M.
	- Within each family there are different generations which are slight variations. 
	- T2 generation has unique features 
	- Within each generation, each instance type is designated by a size such as nano, small, xlarge etc.
	- For eg.  if we select t2.2xlarge instance type, your instance will have balance performance provided by the general purpose category, with the features unique to the T2 family and generation. and specifically it would feature 8vCPUs, 32gbs of memory and moderate network performance.



#### Amazon machine Images(AMI):
- While the Instance types refers to the hardware capability of an instance, AMIs refer to the initial software configurations of an instance.
- When launching an instance for the first time, customer must first specify a soure AMI
- They can launch multiple instances from a single AMI when multiple instances with same configurations are needed. 
- Customers can select AMIs provided by AWS or AWS marketplace or the AWS user community.
- Customers can create and maintin their own custom AMIs.



#### Why Scaling Matters?
- In a traditional datacenter environment, the scalability of a system is bound by the hardware.
- Take the example of tax prepartion business in united states, US tax payers must file their taxes by April 15th every year.
- Online tax preparation companies know that they will experience a steady flow of traffic starting  near the middle of january with traffic peaking near the april 15 deadline.
- In a data center anticipating this 4 month period of heavy use, requires spining up enough physical servers to handle the anticipated load.
- But what happens to those servers for the rest of the year?
- They sit idle in the data center.
- In the cloud because computing power is a programmatic resource, customer can take the more flexible approach towards scaling.
- They can create their programs to create new EC2 instances in advance of known peak period in a business cycle such as tax filing deadlines.
- However adding the use of monitoring, customer can programmatically scale out their servers, when they notice that critical resources such as avg CPU usage across their fleet are becoming constraint.
- Further more they can automatically scale in the number of resources they use during peak times when demand for their business services return to their base line.
- In other words they only pay for the resources, when they need them.


#### Amazon EC2 Auto Scaling group
- Automatically adjusts resource capacity
- Define where Amazon EC2 Auto scaling deploys resources.
- In an auto scaling group, we specify the Amazon VPC and subnets for our amazon EC2 instance deployed by amazon EC2 autoscaling.
- We must select at least two subnets accorss different availability zones.
- Auto scalinggroups help you choose amazon EC2 instance types, we can choose on demand instances, spot instances, or both. 
- Number of instances running in an auto scaling group are controlled by three settings: minimum, maximum and desired capacity.
- Minimum: ensures that we always have a certain number of amazon EC2 instances at all times.
- Maximum: let's amazon ec2 auto scaling, scale  out the number of EC2 instancesas needed to handle increase in demand.
- Desired Capacity: must be equal to greater than the minimum limit, less than or equal to the maximum limit, causing the auto group to launch or terminate instances is like changing the desired capacity. It's value is usaually set by an automated proocess such as an autoscaling policy or Auto scaling event or lambda function. But it can be directly edited in a console where we can observe the effects. 



#### Amazon Elastic Load Blancing (Amazon ELB)
- It automatically distributes traffic across multiple EC2 instances to achiceve better fault tolerance and availability.
- It works by accepting incoming traffic for clients in routes reqest to its register targets such as EC2 instances in one or more availability zones in a region.
- ELB increases the availability and fault tolerance of applications. 
- Customers can confihure health checks, which monitors the health of compute resources so that the load balancer sends request to only the healthy ones.
- They can also offload the work of encryption or decryption to the load balancer so that compute resources can focus on their main wok.\
- Customer can select their load balancer on their application needs:
	- Application Load Balancer (App layer)
		- Especially designed for web app with http and https web traffic and operate at the application layer
	- Network Load Balancers (Network Layer)
	- Gateway load balancers (3rd party virtual appliances) forward traffic to virtual appliances found in aws marketplace.