#### One-to-Many where embedded-document relation approach is preferred.
```shell
> use support
switched to db support

> db.questionThreads.insertOne({creator: "Max", question:"How does that all work?", answers:["q1a1","q1a2"]})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629cac91394aaf44435578d1")
}
> db.questionThreads.findOne()
{
	"_id" : ObjectId("629cac91394aaf44435578d1"),
	"creator" : "Max",
	"question" : "How does that all work?",
	"answers" : [
		"q1a1",
		"q1a2"
	]
}

> db.answers.insertMany([{_id: "q1a1", text: "It works like that."}, {_id: "q1a2", text: "Thanks!"}])
{ "acknowledged" : true, "insertedIds" : [ "q1a1", "q1a2" ] }
> db.anwsers.findOne()
null
> db.answers.findOne()
{ "_id" : "q1a1", "text" : "It works like that." }
> db.answers.find()
{ "_id" : "q1a1", "text" : "It works like that." }
{ "_id" : "q1a2", "text" : "Thanks!" }
> 
> db.questionThreads.deleteMany({})
{ "acknowledged" : true, "deletedCount" : 1 }
> db.questionThreads.insertOne({creator: "Max", question:"How does that all work?", answers:[{text:"Like that"},{text:"Thanks!"}]})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629cae22394aaf44435578d2")
}
> db.questionThreads.findOne()
{
	"_id" : ObjectId("629cae22394aaf44435578d2"),
	"creator" : "Max",
	"question" : "How does that all work?",
	"answers" : [
		{
			"text" : "Like that"
		},
		{
			"text" : "Thanks!"
		}
	]
}

```




#### Relations approach

```shell
> use cityData
switched to db cityData
> db.cities.insertOne({name:"New York City", coordinates:{lat:21, lng:55}})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629caf90394aaf44435578d3")
}
> db.cities.findOne()
{
	"_id" : ObjectId("629caf90394aaf44435578d3"),
	"name" : "New York City",
	"coordinates" : {
		"lat" : 21,
		"lng" : 55
	}
}

> db.citizens.insertMany([{name:"Max", cityId:ObjectId("629caf90394aaf44435578d3")},{name:"Manuel",cityId:ObjectId("629caf90394aaf44435578d3")}])
{
	"acknowledged" : true,
	"insertedIds" : [
		ObjectId("629cb08d394aaf44435578d4"),
		ObjectId("629cb08d394aaf44435578d5")
	]
}

> db.citizens.find().pretty()
{
	"_id" : ObjectId("629cb08d394aaf44435578d4"),
	"name" : "Max",
	"cityId" : ObjectId("629caf90394aaf44435578d3")
}
{
	"_id" : ObjectId("629cb08d394aaf44435578d5"),
	"name" : "Manuel",
	"cityId" : ObjectId("629caf90394aaf44435578d3")
}
```