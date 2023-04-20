`working with passengers collection`
[[flightData]]


let's say passengers have hobbies too.

```shell
> db.passengers.updateOne({name: "Albert Twostone"}, {$set: {hobbies:["sports","cooking"]}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

>
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