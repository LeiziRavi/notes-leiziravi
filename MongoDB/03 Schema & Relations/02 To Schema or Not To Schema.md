![[Pasted image 20220605100406.png]]


### SQL type approach
```shell
> db.products.find().pretty()
{
	"_id" : ObjectId("629c35035bd46acaa4e8b2d0"),
	"name" : "A book",
	"price" : 12.99,
	"details" : null
}
{
	"_id" : ObjectId("629c35125bd46acaa4e8b2d1"),
	"name" : "A T-shirt",
	"price" : 20.99,
	"details" : null
}
{
	"_id" : ObjectId("629c35165bd46acaa4e8b2d2"),
	"name" : "A Computer",
	"price" : 1299,
	"details" : {
		"cpu" : "Intel i7 8770"
	}
}
```


### A Bit more MongoDB approach
```shell
> db.products.find().pretty()
{
	"_id" : ObjectId("629c332b5bd46acaa4e8b2cd"),
	"name" : "A book",
	"price" : 12.99
}
{
	"_id" : ObjectId("629c33695bd46acaa4e8b2ce"),
	"name" : "A T-shirt",
	"price" : 20.99
}
{
	"_id" : ObjectId("629c33be5bd46acaa4e8b2cf"),
	"name" : "A Computer",
	"price" : 1299,
	"details" : {
		"cpu" : "Intel i7 8770"
	}
}

```