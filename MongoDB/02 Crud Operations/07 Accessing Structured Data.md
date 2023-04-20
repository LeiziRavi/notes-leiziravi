```shell
> db.passengers.find({name: "Albert Twostone"}).pretty()
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345456"),
	"name" : "Albert Twostone",
	"age" : 68,
	"hobbies" : [
		"sports",
		"cooking"
	]
}

```

```shell
> db.passengers.findOne({name: "Albert Twostone"}).hobbies
[ "sports", "cooking" ]

```


```shell
> db.passengers.find({hobbies:"sports"}).pretty()
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345456"),
	"name" : "Albert Twostone",
	"age" : 68,
	"hobbies" : [
		"sports",
		"cooking"
	]
}

```

```shell
> db.flightData.find({"status.description":"on-time"}).pretty()
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
			"responsible" : "Max Schwarzmueller"
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
			"responsible" : "Max Schwarzmueller"
		}
	}
}

```


```shell
> db.flightData.find({"status.details.responsible":"Max Schwarzmueller"}).pretty()
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
			"resonsible" : "Max Schwarzmueller"
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
			"responsible" : "Max Schwarzmueller"
		}
	}
}

```