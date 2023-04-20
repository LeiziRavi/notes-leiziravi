![[Projections.png]]

Let say we have 

```json
{
	"_id_" : "...",
	"name" : "Max",
	"age" : 29,
	"job" : "instructor"
}

```

this kind of data in our database, but in the application we need, 

```json
{
	"name" : "Max",
	"age" : 29
}
```

only this.

- Ofcourse, we could fetch all the data, and filter it in our application, but we would need to transfer the complete data over the wire, so we would kind of impact our bandwidth.
- We would fetch unnecessary data and we want to prevent this.
- So it would be better to filter it out on the mongodb server.
- And this is exactly, what ==projection== can help us with. 


```shell
# The second parameter it the find command it projection, which includes, all the fields with value 1 to be included in the find command.

> db.passengers.find({},{name: 1}).pretty()
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345443"),
	"name" : "Max Schwarzmueller"
}
{ "_id" : ObjectId("629b9fe5d24c50d1e5345444"), "name" : "Manu Lorenz" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345445"), "name" : "Chris Hayton" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345446"), "name" : "Sandeep Kumar" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345447"), "name" : "Maria Jones" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345448"), "name" : "Alexandra Maier" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345449"), "name" : "Dr. Phil Evans" }
{ "_id" : ObjectId("629b9fe5d24c50d1e534544a"), "name" : "Sandra Brugge" }
{ "_id" : ObjectId("629b9fe5d24c50d1e534544b"), "name" : "Elisabeth Mayr" }
{ "_id" : ObjectId("629b9fe5d24c50d1e534544c"), "name" : "Frank Cube" }
{ "_id" : ObjectId("629b9fe5d24c50d1e534544d"), "name" : "Karandeep Alun" }
{ "_id" : ObjectId("629b9fe5d24c50d1e534544e"), "name" : "Michaela Drayer" }
{ "_id" : ObjectId("629b9fe5d24c50d1e534544f"), "name" : "Bernd Hoftstadt" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345450"), "name" : "Scott Tolib" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345451"), "name" : "Freddy Melver" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345452"), "name" : "Alexis Bohed" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345453"), "name" : "Melanie Palace" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345454"), "name" : "Armin Glutch" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345455"), "name" : "Klaus Arber" }
{ "_id" : ObjectId("629b9fe5d24c50d1e5345456"), "name" : "Albert Twostone" }
Type "it" for more

# what about id? 
> db.passengers.find({},{name: 1, _id:0}).pretty()
{ "name" : "Max Schwarzmueller" }
{ "name" : "Manu Lorenz" }
{ "name" : "Chris Hayton" }
{ "name" : "Sandeep Kumar" }
{ "name" : "Maria Jones" }
{ "name" : "Alexandra Maier" }
{ "name" : "Dr. Phil Evans" }
{ "name" : "Sandra Brugge" }
{ "name" : "Elisabeth Mayr" }
{ "name" : "Frank Cube" }
{ "name" : "Karandeep Alun" }
{ "name" : "Michaela Drayer" }
{ "name" : "Bernd Hoftstadt" }
{ "name" : "Scott Tolib" }
{ "name" : "Freddy Melver" }
{ "name" : "Alexis Bohed" }
{ "name" : "Melanie Palace" }
{ "name" : "Armin Glutch" }
{ "name" : "Klaus Arber" }
{ "name" : "Albert Twostone" }
Type "it" for more

# So to exclude id, we specifically need to exclude it using _id field and setting it to 0 in projection.

```