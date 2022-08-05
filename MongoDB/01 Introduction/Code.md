```shell
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> use shop
switched to db shop
> db.products.insertOne({"name":"A Book", price: 12.99})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("628603b8f99a9ec254ea5df7")
}

> db.products.find()
{ "_id" : ObjectId("628603b8f99a9ec254ea5df7"), "name" : "A Book", "price" : 12.99 }

> db.products.find().pretty()
{
	"_id" : ObjectId("628603b8f99a9ec254ea5df7"),
	"name" : "A Book",
	"price" : 12.99
}

> db.products.insertOne({"name":"A Pen", price: 12.99, description: "A parker pen"})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("62860410f99a9ec254ea5df8")
}
> db.products.find().pretty()
{
	"_id" : ObjectId("628603b8f99a9ec254ea5df7"),
	"name" : "A Book",
	"price" : 12.99
}
{
	"_id" : ObjectId("62860410f99a9ec254ea5df8"),
	"name" : "A Pen",
	"price" : 12.99,
	"description" : "A parker pen"
}

> db.products.insertOne({"name":"A T-shirt", price: 32.99, size:"M",description: " H & M shirt"})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("62860446f99a9ec254ea5df9")
}

> db.products.find().pretty()
{
	"_id" : ObjectId("628603b8f99a9ec254ea5df7"),
	"name" : "A Book",
	"price" : 12.99
}
{
	"_id" : ObjectId("62860410f99a9ec254ea5df8"),
	"name" : "A Pen",
	"price" : 12.99,
	"description" : "A parker pen"
}
{
	"_id" : ObjectId("62860446f99a9ec254ea5df9"),
	"name" : "A T-shirt",
	"price" : 32.99,
	"size" : "M",
	"description" : " H & M shirt"
}

> db.products.insertOne({"name":"A Computer", price: 1232.99,description: "An Apple computer", details:{cpu:"M1", memory:"32"}})
{
	"acknowledged" : true,
	"insertedId" : ObjectId("62860499f99a9ec254ea5dfa")
}

> db.products.find().pretty()
{
	"_id" : ObjectId("628603b8f99a9ec254ea5df7"),
	"name" : "A Book",
	"price" : 12.99
}
{
	"_id" : ObjectId("62860410f99a9ec254ea5df8"),
	"name" : "A Pen",
	"price" : 12.99,
	"description" : "A parker pen"
}
{
	"_id" : ObjectId("62860446f99a9ec254ea5df9"),
	"name" : "A T-shirt",
	"price" : 32.99,
	"size" : "M",
	"description" : " H & M shirt"
}
{
	"_id" : ObjectId("62860499f99a9ec254ea5dfa"),
	"name" : "A Computer",
	"price" : 1232.99,
	"description" : "An Apple computer",
	"details" : {
		"cpu" : "M1",
		"memory" : "32"
	}
}

```