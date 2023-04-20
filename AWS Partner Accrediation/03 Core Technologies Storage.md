- Anytime a server is set-up either a physical server or virtual server, there needs  to be somewhere the data, the server will access.
- AWS has several storage services:
	- __Amazon Elastic Block Store__ : Persistant block-level storage
		- It's like a hard drive to EC2 instances, 
		- Customers can create partitions on it, format it and boot their operating systems of it.
		- It provide persistant block level storage volumes.
	- __Amazon S3__: Durable scalable object storage
		- It is storage for the internet that is designed to make web scale computing easier for developers
		- It provides simple web interface which can used to store and retreive any amount of data at any time from anywhere on the web.
	- __Amazon S3 Glacier__: Data archiving and backup
		- It provides secure and durable storage for data archiving and backup.
		- It enables organisation to easily and cost effectively retain data for months, years and decades.
	- __AWS Storage Gateway__: Integrate cloud storage with on-site workloads
		- It provides seamless & secure integration between organisations on-premises IT env and an aws storage infrastructure so that large amounts of data can be transferred into and out of the aws cloud.
	- __Amazon Elastic File System__: File storage for Amazon EC2 instances
		- It's a file storage service. 
		- It is easy to use and provides simple interface for creating and configuring file systems.
		- Storage capacity is elastic and grows & sink automatically as files are added and removed.
	- __Amazon FSx__: File Storage for widely-used file systems
		- It is fully managed file system built on four widely used file systems 
			- NetApp ONTAP, OpenZFS, Windows File Server and Lustre
		- The file system selected is typically based on familiarity with a given file system or by mathcing the file systems feature set, performance profiles and data management capabilities to therequirements of the workload.



#### Amazon EBS :
- It provides durable block storage for use with Amazon EC2 instances.
- EBS volumes are network-attached  storage that persist independently from the running life of  a single instance.
- After a volume is attched to the instance, customers can use the volume like a physical harddrive typically formatting it with file system of their choice and using the file i/o interface provided by the instance operating system.
- When customers create an EBS volume in an Availability zone, it is automatically replicated within that zone to prevent data loss due to failure of any single hardware component. 
- After customers create a volume , they can attach it to any EC2 instance in the same Availability zone.
- An Amazon EBS volume can be attached to only one instance at a time, except in the case of using multi-attach with  Provisioned IOPS SSD(io 1) volume to up to 16 Nitro-based instances.
- However multiple volumes can be attached to a single instance.
- By default EBS volumes that are attached to a running instance automatically detach from instance with their data intact when that instance is terminated, the volume then can be attached to a new instance  enabling quick recovery.
- EBS also provides ability to create point-in-time snapshots of volumes which are stored in S3. These snapshots can be used as strating point for new EBS volumes and to protect data for long time durability.
	- Same snapshot can be used to instanstiate as many volumes as desired.
	- These snapshots can be copied across aws regions making it easier to leverage multiple aws regions for geographical expansion, data center migration or disaster recovery.
- Sizes for EBS volumes range from 1GB o 16TB , depending upon the volume type and are allocated in 1GB increments.




#### Amazon S3: (Inifinite scalability, greater analysis, and faster retrieval)
- Amazon S3 is an object storage service.
- It stores data as objects in resources called buckets.
- Customers can store as many objects as they want in bucket and read, write and delete objects in their bucket.
- Objects can be upto 5TB of size, but there no limits to the total storage consume or amount of objects. 
- S3 is designed to provide 
	- 99.999999999 % durability
		- i.e. 11 9s in durability.
		- i.e. It means for every 10 million objects stored, customers can expect to incure an avg loss of a single object once every ten thousand years.	
	- also provides 99.99% availability
		- i.e. 4 9s of availability.
- Common S3 use cases includes:
	- Data lakes hosting
		- Build a centralized repository to store all structured and unstructured data at any scale, to allow big data analytics, AI, ML and high performace computation HPC) applications can run to unlock data insights.
	- Backup and Storage
	- Application Hosting
	- Media hosting
	- Software delivery


#### Storage classes on AMazon S3
```
```
Amazon S3     -->          Amazon S3             -->           Amazon S3          -->             S3          
	Standard                  Standard-                               One Zone-                       Glacier storage 
							Infrequent Acess                    Infrequent Access                         classes

Active Data    --->   Infrequently accessed Data  --->  Archived data

- It is critical to undertand types, volumes and access charcaterisics of customer data. 
- With the variety of Amazon S3 storage types available on AWS, choosing the right storage class is an important architectural decision.
- Even within a single storage service like S3, there are choices.
- __Amazon S3 Standard__ is intended for frequently accessed data.
	- Because it delivers low latency and high troughput, S3 standard is appropriate for a wide variety of use cases.
- __Amazon S3 Standard Infrequent Access, or S3 Standard-IA__ is for data that is accessed less frequently, but requires rapid access when needed.
	- S3 standard IA is similar to S3 standard, but with lower per-gigabyte storage priceand per-gigabyte retrieval fee.
	- It is ideal for long term storage, backups, and as a data store for disaster recovery files.
- __Amazon S3 One-Zone infrequent Access or S3 One-Zone IA__ is also for data that is accessed less frequently.
	- Other S3 storage classes store data in a minimum of 3-Availability zones, while S3 One-Zone IA stores data in a single AZ resulting in 99.5% availability.
	- It costs less than S3 standard-IA.
	- It is  ideal for the customers who do not require the availability and resilience of S3 standard or S3 standard IA.
	- It is a good choice for storing secondary backup copies of  on-premises data or easily recreatable data.
- __S3 Glacier__
	- S3 glacier is secure, durable, and low-cost storage classes for data archiving.
	- It provides three-retrieval options:
		- Amazon S3 instant retrieval
		- Amazon S3 glacier flexible retrieval
		- Amazon S3 deep archive
	- These options range from a few minutes to hours.
	- It can replace tape for media and entertainment applications and assist for compliance in highly regulated organizations like healthcare, life sciences, and financial services,
- Also offered is Amazon S3 intelligent tiering, which delivers automatic cost savings by moving data between two accessed tiers configured by the customer.