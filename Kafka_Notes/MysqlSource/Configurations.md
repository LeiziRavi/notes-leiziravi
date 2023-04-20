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

# plugins are very important here, since kafka by defualt doesn't contains the mysql/connector jar files, so here we have to provide the path to jdbc or mysql connector 

```

 
4. Worker Configuration
	1. Mysql Source
		-  create a json file with  following contents for __source worker__

```json

// For details: https://docs.confluent.io/kafka-connect-jdbc/current/source-connector/source_config_options.html

{
  "name": "mysql-bulk-source", // name of connector
  "config": {
    "connector.class":"io.confluent.connect.jdbc.JdbcSourceConnector",
    "tasks.max":"1",
    // get the connection details from mysql workbench/server 
    "connection.url":"jdbc:mysql://localhost:3306/mydb",
    "connection.user":"root",
    "connection.password":"root",
    "mode":"bulk",
    "topic.prefix":"mysql-"
  }
}
``` 
 
2. File Sink
   - create a json file with following contents for __sink worker__

```json
{
    "name": "student-file-sink",
    "config": {
        "connector.class": "FileStreamSink",
        "tasks.max": 1,
        "file": "student.txt",
        "topics": "mysql-student"
    }
}
```



