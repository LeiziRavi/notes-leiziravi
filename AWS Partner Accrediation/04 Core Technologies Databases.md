- AWS offers wide-variety of databases that are
	- Purpose-built for specific application use cases
	- handles time consuming database management tasks, such as backup, patch management, and replication,  allowing customers to pursue higher value application management or database refinements.

- __Amazon  Relational Database Service (RDS)__ is a managed database service with a choice of six popular database engines, including Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and SQL Server.
	- Customers can set-up, scale and operate a relational database in the cloud that provides cost-efficient and resizable capacity.
	- Amazon RDS has many otherfeatures that enhance relaibility for critical production databases, including automated backups, database snapshots, and automatic host replacement.

- __DynamoDB__ is a NoSQL database that delivers single digit millisecodn performance at any scale. 
	- With a few clicks in a new clicks in the AWS management concole, customers can launch a new Amazon DynamoDB database table,  scale their requested capacity without downtime or performance degradation, and gain visibility into resource usage and performance metrics.


- __Amazon ElasticCache__ is a caching service that makes it easy to deploy, operate and scale an in-memory cache in the cloud.
	- It improves the performance of web applications by allowing customers to retrieve information from a fast managed in-memory caching system instead of relying entirely on slower disk-based systems.


LINK: aws.amazon.com/databases


#### EC2-Hosted vs AWS Database Services
| AWS Database Services                                                                                                                                                             | Databases on Amazon EC2                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| easier to set-up, manage and maintain                                                                                                                                             | Full control over the database, including SIS/system user access |
| Reduce undifferentiated heacy lifting such as provisioning the database, performing back up and recovery tasks, and managing security patches, storage and minor version updates. | Access at the operating system level                                                                |
| It is highly available database solution with push-botton synchronous multiple AZ deployment without having to manually set up and maintain a standby database.                   | Use of commercial software features or options that are not currently supported by AWS.                                                                |
| Synchronous replication to a standby instance for high availability for oracle database SE1 and SE2                                                                               |                                                                  |
| No need to manage backups, and most importantly, point-in-time recoveries of the database.                                                                                        |                                                                  |
| Scaling the instance type up or down on workload patterns without being concerned about licensing and the complexity involved.                                                    |                                                                  |



