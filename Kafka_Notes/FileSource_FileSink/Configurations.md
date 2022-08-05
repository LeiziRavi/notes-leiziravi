1. Zookeeper configuration
	[[Zookeeper Configuration |]]
2. Kafka broker/server configuration
	[[Kafka Configuration |]]
3. Connect Distributed 
	- edit __/kafka/config/connect-distributed.properties__
	- following properties are default properties and most of the properties need not bother you
	- remember to edit __bootstrap-server__ and add __ipaddress of host machine__.
	- for distributed  connection, __group.id__ is also needed.
	
```properties

bootstrap.servers=172.20.10.13:9092
group.id=connect-cluster
key.converter.schemas.enable=true
value.converter.schemas.enable=true
offset.storage.topic=connect-offsets
offset.storage.replication.factor=1
config.storage.topic=connect-configs
config.storage.replication.factor=1
status.storage.topic=connect-status
status.storage.replication.factor=1
listeners=HTTP://localhost:8083
plugin.path=/usr/local/share/java,/usr/local/share/kafka/plugins,/opt/connectors,

```

 
4. Worker Configuration
	1. File Source
		-  create a json file with  following contents for __source worker__

```json
	{
	    "name": "load-file-source", // name of source connector
	    "config": {
	        "connector.class": "FileStreamSource", // source connector type
	        "tasks.max": 1,
	        "file": "NOTICE", // absolute file path of the source file 
	        "topic": "reconnect-topic" //topic to save the data into
	    }
	}
		
```

> 
> topic will be created with the default properties if not created manually.
> 
 
2. File Sink
   - create a json file with following contents for __sink worker__

```json
	{
	    "name": "load-file-sink", // name of sink connector
	    "config": {
	        "connector.class": "FileStreamSink", // sink connector type
	        "tasks.max": 1,
	        "file": "distributed-sink.txt", // absolute file path of the sink file
	        "topics": "reconnect-topic" //topic to access data from
	    }
	}

```



