### 1. Create/Edit all the configurations files as mentioned in configurations
![[FileSource_FileSink/Configurations]]

### 2. Start Source connector

```bash
curl -d @"/home/leiziravi/work/kafka/source-kafka-config.json" /
	 -H "Content-Type: application/json" /
	 -X POST http://localhost:8083/connectors

# curl is used in command lines or scripts to transfer data
# -X : {reequest method} and {request target}
# -H : {custom header}
# -d : HTTP POST DATA, '@' allowed
# curl --help all : {for all the available options for curl}
```

- To check if the connector is indeed started (Also, if any connector is running)
```shell
	curl http://localhost:8083/connectors
```

- To verify the creation of topic

```bash
/bin/kafka-topics.sh --list --bootstrap-server {ipadress}:{portnumber_kafka_server}

```

- To verify data in the topic
```bash
/bin/kafka-console-consumer --topic {name-of-topic-passed-in-source-and-sink} --from-beginning --bootstrap-server {ipadress}:{portnumber_kafka_server}
```

### 3. Start Sink Connector
```bash
curl -d @"/home/leiziravi/work/kafka/source-kafka-config.json" /
	 -H "Content-Type: application/json" /
	 -X POST http://localhost:8083/connectors

# curl is used in command lines or scripts to transfer data
# -X : {reequest method} and {request target}
# -H : {custom header}
# -d : HTTP POST DATA, '@' allowed
# curl --help all : {for all the available options for curl}
```
- After running sink connector, the file with name passed in sink worker connection will be created with the data acquired from the passed topic.

### 4. Close/Delete Source & Sink Connector after use

```shell
# pass name of source connector with rest uri
curl -X DELETE http://localhost:8083/connectors/local-file-source 

# pass name of sink connector with rest uri
curl -X DELETE http://localhost:8083/connectors/local-file-sink

```

>
>__Error log:__
>
>1. `{"error_code":500,"message":"Request timed out"}`
>	Remember to match servers and __offset.storage.replication.factor__ , in case you are on a standalone server, keep __offset.storage.replication.factor=1__ , and for multiple brokers, keep the number accordingly.
>2.  `{"error_code":409,"message":"Connector local-file-source already exists"}`
>	After implementing source and sink connectors, remember to __delete__ the connectors
>3.  `{"error_code":405,"message":"HTTP 405 Method Not Allowed"}`
>	Use __POST__ method to send properties to REST		
>	

_Happy Hacking._

