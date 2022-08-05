- Nested documents
- Can have upto 100 levels of Nesting
- Overall document size has to be below 16mb
- We can also have ==Array of Embedded documents, or Arrays of any data==

```shell
# to begin with

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

```shell
# josn document, wrapping another json document
> db.flightData.updateMany({},{$set: {status: {description: "on-time", lastUpdated: "1 hour ago"}}})
{ "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true,
	"status" : {
		"description" : "on-time",
		"lastUpdated" : "1 hour ago"
	}
}
{
	"_id" : ObjectId("629b9294394269cd4a2e104a"),
	"departureAirport" : "LHR",
	"arrivalAirport" : "TXL",
	"aircraft" : "Airbus A320",
	"distance" : 950,
	"intercontinental" : false,
	"status" : {
		"description" : "on-time",
		"lastUpdated" : "1 hour ago"
	}
}

```

```shell
# embedded document inside another embedded document
> db.flightData.updateMany({},{$set: {status: {description: "on-time", lastUpdated: "1 hour ago", details:{reponsible: "Max Schwarzmueller"}}}})
{ "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }
> db.flightData.find().pretty()
{
	"_id" : ObjectId("629b9294394269cd4a2e1049"),
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : true,
	"status" : {
		"description" : "on-time",
		"lastUpdated" : "1 hour ago",
		"details" : {
			"reponsible" : "Max Schwarzmueller"
		}
	}
}
{
	"_id" : ObjectId("629b9294394269cd4a2e104a"),
	"departureAirport" : "LHR",
	"arrivalAirport" : "TXL",
	"aircraft" : "Airbus A320",
	"distance" : 950,
	"intercontinental" : false,
	"status" : {
		"description" : "on-time",
		"lastUpdated" : "1 hour ago",
		"details" : {
			"reponsible" : "Max Schwarzmueller"
		}
	}
}

```