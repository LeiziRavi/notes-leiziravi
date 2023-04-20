```shell
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

#### UpdateOne
```shell
> db.flightData.updateOne({ _id: ObjectId("629b9294394269cd4a2e1049")},{$set: {delayed: true}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true,
	"delayed" : true
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


#### Update
```shell
> db.flightData.update({ _id: ObjectId("629b9294394269cd4a2e1049")},{$set: {delayed: true}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 0 })
> db.flightData.update({ _id: ObjectId("629b9294394269cd4a2e1049")},{$set: {delayed: false}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true,
	"delayed" : false
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

>
Update works a bit like update many, updateMany was used to update all matching elements, and update also would update all matching elements.
>


##### What is the difference between update and UpdateMany?
```shell
# After removing '$set', we run the updateOne and updateMany commands with the same update field, it throws an error.
> db.flightData.updateOne({ _id: ObjectId("629b9294394269cd4a2e1049")},{delayed: false})
uncaught exception: Error: the update operation document must contain atomic operators :
DBCollection.prototype.updateOne@src/mongo/shell/crud_api.js:565:19
@(shell):1:1

> db.flightData.updateMany({ _id: ObjectId("629b9294394269cd4a2e1049")},{delayed: false})
uncaught exception: Error: the update operation document must contain atomic operators :
DBCollection.prototype.updateMany@src/mongo/shell/crud_api.js:655:19
@(shell):1:1


# But when we follow the same with update command, it works.
> db.flightData.update({ _id: ObjectId("629b9294394269cd4a2e1049")},{delayed: false})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

```

## BUT
```shell
> db.flightData.find().pretty()
{ "_id" : ObjectId("629b9294394269cd4a2e1049"), "delayed" : false }
{
	"_id" : ObjectId("629b9294394269cd4a2e104a"),
	"departureAirport" : "LHR",
	"arrivalAirport" : "TXL",
	"aircraft" : "Airbus A320",
	"distance" : 950,
	"intercontinental" : false
}

```

==__update__ overrides the data, i.e. it takes the new object and replaces the old object with the new one, keeping the '_id' same== 

__- It is advised not to use 'update', but use 'updateOne' and 'updateMany'__

__- If we really want to replace the data, use 'replaceOne'__

```shell
> db.flightData.replaceOne({ _id: ObjectId("629b9294394269cd4a2e1049")},{
... "departureAirport" : "MUC",
... "arrivalAirport" : "SFO",
... "aircraft" : "Airbus A380",
... "distance" : 12000,
... "intercontinental" : true})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
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