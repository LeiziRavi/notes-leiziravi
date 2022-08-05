link:https://docs.oracle.com/javase/tutorial/reflect/
__API__: an already developed class/program used to develop new classes/prgram.

__{COncept_Name} + API__ : Group of classes

==Reflection is commonly used by programs which require the ability to examine or modify the runtime behavior of applications running in the Java virtual machine.==

- Java reflection, allows us to inspect and/or modify runtime attributes of classes, interfaces, fields and methods. This particularly comes in handy when we don't know their names at compile time.
- Additionally, we can instantiate new objects, invoke methods and get or set field values using reflection.
-----------------------------------------------------------------------
#### Project setup:
**To use Java reflection, we don't need to include any special jars**, any special configuration or Maven dependencies. The JDK ships with a group of classes that are bundled in the [_java.lang.reflect_](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/reflect/package-summary.html) package specifically for this purpose.

So, all we need to do is to make the following import into our code:

```java
import java.lang.reflect.*;
```

And we are good to go.

To get access to the class, method and field information of an instance, we call the _getClass_ method, which returns the runtime class representation of the object. The returned _class_ object provides methods for accessing information about a class.

-----------------------------------------------------------------------
#### Simple Example

```java

public class Person {
    private String name;
    private int age;
}
```

We'll now use Java reflection to discover the names of all fields of this class.

```java
@Test
public void givenObject_whenGetsFieldNamesAtRuntime_thenCorrect() {
    Object person = new Person();
    Field[] fields = person.getClass().getDeclaredFields();

    List<String> actualFieldNames = getFieldNames(fields);

    assertTrue(Arrays.asList("name", "age")
      .containsAll(actualFieldNames));
}
```

```java
private static List<String> getFieldNames(Field[] fields) {
    List<String> fieldNames = new ArrayList<>();
    for (Field field : fields)
      fieldNames.add(field.getName());
    return fieldNames;
}
```

This test shows us that we are able to get an array of _Field_ objects from our _person_ object, even if the reference to the object is a parent type of that object.

In the above example, we were only interested in the names of those fields. But there is much more that can be done.

-----------------------------------------------------------------------
#### JAVA Reflection use cases
- For instance, in many cases, we have a naming convention for database tables. We may choose to add consistency by prefixing our table names with tbl_ so that a table with student data is called tbl_student_data.
	
	In such cases, we could name the Java object holding student data as _Student_ or _StudentData_. Then using the CRUD paradigm, we have one entry point for each operation so that _Create_ operations only receive an _Object_ parameter.

	We then use reflection to retrieve the object name and field names. At this point, we can map this data to a DB table and assign the object field values to the appropriate DB field names.

----------------------------------------------------------------------- 
#### Inspecting JAVA Classes
1. Getting ready
2. 