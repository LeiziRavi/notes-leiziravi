# Gson

Gson is a Java library that can be used to convert Java Objects into their JSON representation. It can also be used to convert a JSON string to an equivalent Java object. ==Gson can work with arbitrary Java objects including pre-existing objects that you do not have source-code of==.

There are a few open-source projects that can convert Java objects to JSON. However, most of them require that you place Java annotations in your classes; something that you can not do if you do not have access to the source-code. Most also do not fully support the use of Java Generics. Gson considers both of these as very important design goals.

Gson is currently in maintenance mode; existing bugs will be fixed, but large new features will likely not be added. If you want to add a new feature, please first search for existing GitHub issues, or create a new one to discuss the feature and get feedback.

### Goals
-   Provide simple `toJson()` and `fromJson()` methods to convert Java objects to JSON and vice-versa
-   Allow pre-existing unmodifiable objects to be converted to and from JSON
-   Extensive support of Java Generics
-   Allow custom representations for objects
-   Support arbitrarily complex objects (with deep inheritance hierarchies and extensive use of generic types)

### Download

Gradle:
```xml
dependencies {
  implementation 'com.google.code.gson:gson:2.9.0'
}
```

Maven
```xml
<dependency>
  <groupId>com.google.code.gson</groupId>
  <artifactId>gson</artifactId>
  <version>2.9.0</version>
</dependency>
```

##### Link: https://github.com/google/gson
#### Docs: https://github.com/google/gson/blob/master/UserGuide.md


