

![[Crud Operations.png]]

#### Initial Data

```json
[
{
	"_id" : ObjectId("629b89f4394269cd4a2e1046"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
},
{
	"_id" : ObjectId("629b8ba9394269cd4a2e1047"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR"
},
{
	"_id" : "txl-lhr-1",
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR"
}
]
```

#### Delete One

```shell


> db.flightData.deleteOne({arrivalAirport: "LHR"})
{ "acknowledged" : true, "deletedCount" : 1 }
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
	"_id" : "txl-lhr-1",
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR"
}

```



#### Update One
```shell

> db.flightData.updateOne({distance:12000},{marker: 'delete'})
uncaught exception: Error: the update operation document must contain atomic operators :
DBCollection.prototype.updateOne@src/mongo/shell/crud_api.js:565:19
@(shell):1:1

# To update we need to use "$set" followed by the json of field/data to be used as update.


> db.flightData.updateOne({distance:12000},{$set: {marker: 'delete'}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b89f4394269cd4a2e1046"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true,
	"marker" : "delete"
}
{
	"_id" : "txl-lhr-1",
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR"
}

```


#### Update Many
```shell
> db.flightData.updateMany({},{$set: {marker: 'toDelete'}})
{ "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }
> db.flightData.find().pretty()
{
	"_id" : "txl-lhr-1",
	"departureAirport" : "MUC",
	"arrivalAirport" : "LHR",
	"marker" : "toDelete"
}
{
	"_id" : ObjectId("629b90f7394269cd4a2e1048"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true,
	"marker" : "toDelete"
}

```


#### Delete Many
```shell
> db.flightData.deleteMany({"marker":"toDelete"})
{ "acknowledged" : true, "deletedCount" : 2 }
> db.flightData.find().pretty()
> 


# Delete Many can also be achieved, if wish to delete all the documents in a collection regardless of filter
> db.filghtData.deleteMany({})
```


#### Insert many
```shell
> db.flightData.insertMany([
... {
... "departureAirport":"MUC",
... "arrivalAirport": "SFO",
... "aircraft":"Airbus A380",
... "distance": 12000,
... "intercontinental": true
... },
... {
... "departureAirport": "LHR",
... "arrivalAirport": "TXL",
... "aircraft": "Airbus A320",
... "distance": 950,
... "intercontinental": false
... }
... ])
{
	"acknowledged" : true,
	"insertedIds" : [
		ObjectId("629b9294394269cd4a2e1049"),
		ObjectId("629b9294394269cd4a2e104a")
	]
}


> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}
{
	"_id" : ObjectId("629b9294394269cd4a2e104a"),
	"departureAirport" : "LHR",
	"arrivalAirport" : "TXL",
	"aircraft" : "Airbus A320",
	"distance" : 950,
	"intercontinental" : false
}

```


#### find with filter
```shell
> db.flightData.find({intercontinental: true}).pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}

> db.flightData.find({distance: 12000}).pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}

> db.flightData.find({distance: {$gt :10000}}).pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}


> db.flightData.find({distance: {$gt :900}}).pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}
{
	"_id" : ObjectId("629b9294394269cd4a2e104a"),
	"departureAirport" : "LHR",
	"arrivalAirport" : "TXL",
	"aircraft" : "Airbus A320",
	"distance" : 950,
	"intercontinental" : false
}


```

#### Find One

```shell
> db.flightData.findOne({distance: {$gt :900}})
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true
}

```