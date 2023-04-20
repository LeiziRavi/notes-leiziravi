```shell
> db.passengers.find().pretty()
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345443"),
	"name" : "Max Schwarzmueller",
	"age" : 29
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345444"),
	"name" : "Manu Lorenz",
	"age" : 30
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345445"),
	"name" : "Chris Hayton",
	"age" : 35
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345446"),
	"name" : "Sandeep Kumar",
	"age" : 28
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345447"),
	"name" : "Maria Jones",
	"age" : 30
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345448"),
	"name" : "Alexandra Maier",
	"age" : 27
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345449"),
	"name" : "Dr. Phil Evans",
	"age" : 47
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544a"),
	"name" : "Sandra Brugge",
	"age" : 33
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544b"),
	"name" : "Elisabeth Mayr",
	"age" : 29
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544c"),
	"name" : "Frank Cube",
	"age" : 41
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544d"),
	"name" : "Karandeep Alun",
	"age" : 48
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544e"),
	"name" : "Michaela Drayer",
	"age" : 39
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544f"),
	"name" : "Bernd Hoftstadt",
	"age" : 22
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345450"),
	"name" : "Scott Tolib",
	"age" : 44
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345451"),
	"name" : "Freddy Melver",
	"age" : 41
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345452"),
	"name" : "Alexis Bohed",
	"age" : 35
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345453"),
	"name" : "Melanie Palace",
	"age" : 27
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345454"),
	"name" : "Armin Glutch",
	"age" : 35
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345455"),
	"name" : "Klaus Arber",
	"age" : 53
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345456"),
	"name" : "Albert Twostone",
	"age" : 68
}
Type "it" for more
# If we check the printed data in the console with the actual data, we see that one data is not printed in the console, but we see "type 'it' for more"

> it
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345457"),
	"name" : "Gordon Black",
	"age" : 38
}

```


- __find does not  give us an array of all the documents in a collection but returns only a ==cursor-object==__
- This makes a lot of sense because that collection could be very big and if find would immediately send us back all documents and let say the collection has 20 million documents, then this would take super long but most importantly, it would send a lot of data over the wire.
- So, instead of that, it gives us back cursor object which is an object with a lot of metadata behind it that allows us to cycle through the results and that is what "it" command did.
- It basically used that cursor to fetch the next bunch of data.


#### find().toArray()
```shell
> db.passengers.find().toArray()
[
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345443"),
		"name" : "Max Schwarzmueller",
		"age" : 29
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345444"),
		"name" : "Manu Lorenz",
		"age" : 30
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345445"),
		"name" : "Chris Hayton",
		"age" : 35
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345446"),
		"name" : "Sandeep Kumar",
		"age" : 28
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345447"),
		"name" : "Maria Jones",
		"age" : 30
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345448"),
		"name" : "Alexandra Maier",
		"age" : 27
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345449"),
		"name" : "Dr. Phil Evans",
		"age" : 47
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e534544a"),
		"name" : "Sandra Brugge",
		"age" : 33
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e534544b"),
		"name" : "Elisabeth Mayr",
		"age" : 29
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e534544c"),
		"name" : "Frank Cube",
		"age" : 41
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e534544d"),
		"name" : "Karandeep Alun",
		"age" : 48
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e534544e"),
		"name" : "Michaela Drayer",
		"age" : 39
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e534544f"),
		"name" : "Bernd Hoftstadt",
		"age" : 22
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345450"),
		"name" : "Scott Tolib",
		"age" : 44
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345451"),
		"name" : "Freddy Melver",
		"age" : 41
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345452"),
		"name" : "Alexis Bohed",
		"age" : 35
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345453"),
		"name" : "Melanie Palace",
		"age" : 27
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345454"),
		"name" : "Armin Glutch",
		"age" : 35
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345455"),
		"name" : "Klaus Arber",
		"age" : 53
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345456"),
		"name" : "Albert Twostone",
		"age" : 68
	},
	{
		"_id" : ObjectId("629b9fe5d24c50d1e5345457"),
		"name" : "Gordon Black",
		"age" : 38
	}
]

```

#### find().forEach()

```shell
# In forEach, we can use a function to process each data.
# It doesn't load data in advance unlike toArray()
# But fetches it on-demand.

>  db.passengers.find().forEach((passengerData) => {printjson(passengerData)})
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345443"),
	"name" : "Max Schwarzmueller",
	"age" : 29
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345444"),
	"name" : "Manu Lorenz",
	"age" : 30
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345445"),
	"name" : "Chris Hayton",
	"age" : 35
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345446"),
	"name" : "Sandeep Kumar",
	"age" : 28
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345447"),
	"name" : "Maria Jones",
	"age" : 30
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345448"),
	"name" : "Alexandra Maier",
	"age" : 27
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345449"),
	"name" : "Dr. Phil Evans",
	"age" : 47
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544a"),
	"name" : "Sandra Brugge",
	"age" : 33
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544b"),
	"name" : "Elisabeth Mayr",
	"age" : 29
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544c"),
	"name" : "Frank Cube",
	"age" : 41
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544d"),
	"name" : "Karandeep Alun",
	"age" : 48
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544e"),
	"name" : "Michaela Drayer",
	"age" : 39
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e534544f"),
	"name" : "Bernd Hoftstadt",
	"age" : 22
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345450"),
	"name" : "Scott Tolib",
	"age" : 44
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345451"),
	"name" : "Freddy Melver",
	"age" : 41
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345452"),
	"name" : "Alexis Bohed",
	"age" : 35
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345453"),
	"name" : "Melanie Palace",
	"age" : 27
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345454"),
	"name" : "Armin Glutch",
	"age" : 35
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345455"),
	"name" : "Klaus Arber",
	"age" : 53
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345456"),
	"name" : "Albert Twostone",
	"age" : 68
}
{
	"_id" : ObjectId("629b9fe5d24c50d1e5345457"),
	"name" : "Gordon Black",
	"age" : 38
}

```
