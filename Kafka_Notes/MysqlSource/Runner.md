curl -d @"/home/leiziravi/work/kafka/source-kafka-jdbc.json" -H "Content-Type: application/json" -X POST http://localhost:8083/connectors


curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @/home/leiziravi/work/kafka/source-kafka-jdbc.json

curl -d @"/home/leiziravi/work/kafka/source-kafka-config.json" -H "Content-Type: application/json" -X POST http://localhost:8083/connectors