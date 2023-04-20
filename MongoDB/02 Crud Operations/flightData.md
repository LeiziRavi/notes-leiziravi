```json
[
	{
		"departureAirport":"MUC",
		"arrivalAirport": "SFO",
		"aircraft":"Airbus A380",
		"distance": 12000,
		"intercontinental": true
	},
	{
		"departureAirport": "LHR",
		"arrivalAirport": "TXL",
		"aircraft": "Airbus A320",
		"distance": 950,
		"intercontinental": false
	}
]
```



```shell
>  use flights
switched to db flights
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> db.flightData.insertOne({
... "departureAirport":"MUC",
... "arrivalAirport": "SFO",
... "aircraft":"Airbus A380",
... "distance": 12000,
... "intercontinental": true
... })
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629b89f4394269cd4a2e1046")
}
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b89f4394269cd4a2e1046"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}
> db.flightData.insertOne({ "departureAirport":"MUC", "arrivalAirport":"LHR"})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629b8ba9394269cd4a2e1047")
}
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b89f4394269cd4a2e1046"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}
{
	"_id" : ObjectId("629b8ba9394269cd4a2e1047"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR"
}
> db.flightData.insertOne({ "departureAirport":"MUC", "arrivalAirport":"LHR", "_id":"txl-lhr-1"})
{ "acknowledged" : true, "insertedId" : "txl-lhr-1" }
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b89f4394269cd4a2e1046"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}
{
	"_id" : ObjectId("629b8ba9394269cd4a2e1047"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR"
}
{
	"_id" : "txl-lhr-1",
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR"
}
> db.flightData.insertOne({ "departureAirport":"MUC", "arrivalAirport":"LHR", "_id":"txl-lhr-1"})
WriteError({
	"index" : 0,
	"code" : 11000,
	"errmsg" : "E11000 duplicate key error collection: flights.flightData index: _id_ dup key: { _id: \"txl-lhr-1\" }",
	"op" : {
		"departureAirport" : "MUC",
		"arrivalAirport" : "LHR",
		"_id" : "txl-lhr-1"
	}
}) :
WriteError({
	"index" : 0,
	"code" : 11000,
	"errmsg" : "E11000 duplicate key error collection: flights.flightData index: _id_ dup key: { _id: \"txl-lhr-1\" }",
	"op" : {
		"departureAirport" : "MUC",
		"arrivalAirport" : "LHR",
		"_id" : "txl-lhr-1"
	}
})
WriteError@src/mongo/shell/bulk_api.js:465:48
mergeBatchResults@src/mongo/shell/bulk_api.js:871:49
executeBatch@src/mongo/shell/bulk_api.js:940:13
Bulk/this.execute@src/mongo/shell/bulk_api.js:1182:21
DBCollection.prototype.insertOne@src/mongo/shell/crud_api.js:264:9
@(shell):1:1

```