- MongoDB is a document-oriented database, not a relational one.
- A document-oriented database replaces the concept of a "row" with a more flexible model, the "document." 
	- By  allowing embedded documents and arrays, the document-oriented approach makes it possible to represent complex hiierarchical relationships with a single record.
	- There are no predefined schemas: a documet's keys and values are not of fixed types or sizes.
	- Without a fixed schema, adding or removing fields as needed becomes easier.

#### Designed to Scale:
- Scaling a database comes down to the choice between scaling up (getting a bigger machhine) or scaling out (partitioning data across more machines).
	- Scaling up is often the path of least resistance.
		- __Drawbacks of Scaling up__: 
		- Large machines are often very expensive, and eventually a physical limit is reached where a more powerful machine cannot purchased at any cost.
	- Scaling out: to add storage space or increase throughput for read and write operations, buy additional servers, and add them to one's cluster.
		- This is both cheaper and more scalable.
		- __Drawbacks of Scaling out:__
			- It is difficult to administer a thousand machines than it is care for one.
	- MongoDB was designed to scale out.
	- Document-oriented data model makes it easier to split data across multiple servers.
	- MongoDB automatically takes care of balancing data and load across a cluster, redistributing documents automatically and routing reads and write to the correct machines.

![[Scaling out MongoDB using sharding across multiple servers.png]]

#### MongoDB is rich with features:
- __Indexing__:
	- supports generic secondary indexes and provide unique, compound, geospatial, and full-text indexing capabilities as well.
	- Secondary indexes on hierarchical structures such as nested documents and arrays are also supported. 

- __Aggregation__:
	- Provides an aggregation framework based on the concept of data processing pipelines.
	- this pipelines allow one to build complex analytics engines by processing data through a series of relatively simple stages on the server side, taking full advantage of database optimizations.

- __Special collection and index types__:
	- MongoDB supports time-to-live(TTL) collections for data that should expire at a certain time, such as sessions and fixed-size (caped) collections, for holding recent data, such as logs.
	- It also supports partial indexes limited to only those documets matching a criteria filter in order to increase efficiency and reduce the amount of storage space required.

- __File Storage__:
	- It also supports an easy-to-use protocol for storing large files and file metadata.


## Main focus for MongoDB project: is to create a full-featured data store that is scalable, flexible and fast.