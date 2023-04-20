- Snowflake’s architecture is a hybrid model of both a shared-disk and a shared nothing architecture. 
- At the core of Snowflake’s architecture are three separate layers: 
	- __Cloud Services:__ 
		- The cloud services layer of Snowflake handles all of the services within the database such as metadata management, authentication, security, and query optimization.
	- __Compute:__ 
		- Snowflake has virtual warehouses that run the compute. The query layer is separated from the disk storage.
	- __Storage:__ 
		- Snowflake uses micropartitions, which are heavily compressed and optimized to organize the data into a columnar data store. ==The data is stored within the cloud provider’s cloud storage (e.g., S3 in AWS). Compute nodes connect to the storage layer to retrieve the data and process it.==

![[SnowFlake's Three Layer Architecture.png]]

