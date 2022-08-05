![[Pasted image 20220605161216.png]]


#### Refernce Approach
```shell
> use hospital
switched to db hospital
> db.patients.insertOne({name: "Max", age: 29, diseaseSummary: "summary-max-1"})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629c8aab5bd46acaa4e8b2d6")
}
> db.patients.findOne()
{
	"_id" : ObjectId("629c8aab5bd46acaa4e8b2d6"),
	"name" : "Max",
	"age" : 29,
	"diseaseSummary" : "summary-max-1"
}
> db.diseaseSummary.insertOne({_id: "summary-max-1", diseases: ["cold", "broken leg"]})
{ "acknowledged" : true, "insertedId" : "summary-max-1" }

> db.diseaseSummary.findOne()
{ "_id" : "summary-max-1", "diseases" : [ "cold", "broken leg" ] }

> db.patients.findOne()
{
	"_id" : ObjectId("629c8aab5bd46acaa4e8b2d6"),
	"name" : "Max",
	"age" : 29,
	"diseaseSummary" : "summary-max-1"
}

> db.patients.findOne().diseaseSummary
summary-max-1

> var dsid = db.patients.findOne().diseaseSummary
> dsid
summary-max-1

> db.diseaseSummary.findOne({_id:dsid})
{ "_id" : "summary-max-1", "diseases" : [ "cold", "broken leg" ] }

```

```shell
> db.persons.insertOne({name: "Max",age:29, salary:3000})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629c95d9394aaf44435578cf")
}
> db.cars.insertOne({model: "BMW",price: 40000, owner: ObjectId("629c95d9394aaf44435578cf")})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629c9614394aaf44435578d0")
}
```



#### Embedded Document Approach
- When two documents have strong 1-to-1 relationship.
```shell
> db.patients.insertOne({name: "Max", age: 29, diseaseSummary: {diseases: ["cold","broken leg"]}})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("629c8c89394aaf44435578cd")
}
> db.patients.findOne()
{
	"_id" : ObjectId("629c8c89394aaf44435578cd"),
	"name" : "Max",
	"age" : 29,
	"diseaseSummary" : {
		"diseases" : [
			"cold",
			"broken leg"
		]
	}
}
> db.patients.findOne().diseaseSummary
{ "diseases" : [ "cold", "broken leg" ] }

```