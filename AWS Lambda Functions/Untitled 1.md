As others have suggested, you can simply use the add method in the JsonArray builder.

```java
import javax.json.*;

public class JsonExample {
    public static void main(String[] args) {
        JsonObject personObject = Json.createObjectBuilder()
                .add("name", Json.createObjectBuilder()
                        .add("given", "John")
                        .add("middle", "Edward")
                        .add("surname", "Doe")
                        .build())
                .add("age", 42)
                .add("isMarried", true)
                .add("address", Json.createObjectBuilder()
                        .add("street", "Main Street")
                        .add("city", "New York")
                        .add("zipCode", "10044")
                        .add("country", "United States")
                        .build())
                .add("phoneNumber", Json.createArrayBuilder()
                        .add("+1 (718) 111-1111")
                        .add("+1 (718) 111-1112")
                        .build())
                .build();

        JsonArray personArray = Json.createArrayBuilder()
                .add(personObject) // Add person to array.
                .build();

        System.out.println(JsonUtil.prettyPrint(personArray));
    }
}
```

This is simply used to format the JSON output.

```java
import java.io.StringWriter;
import java.util.*;
import javax.json.*;
import javax.json.stream.JsonGenerator;

/* Based on: http://stackoverflow.com/a/32500882/1762224 */
public class JsonUtil {
    public static String prettyPrint(JsonStructure json) {
        return jsonFormat(json, JsonGenerator.PRETTY_PRINTING);
    }

    public static String jsonFormat(JsonStructure json, String... options) {
        StringWriter stringWriter = new StringWriter();
        Map<String, Boolean> config = buildConfig(options);
        JsonWriterFactory writerFactory = Json.createWriterFactory(config);
        JsonWriter jsonWriter = writerFactory.createWriter(stringWriter);

        jsonWriter.write(json);
        jsonWriter.close();

        return stringWriter.toString();
    }

    private static Map<String, Boolean> buildConfig(String... options) {
        Map<String, Boolean> config = new HashMap<String, Boolean>();

        if (options != null) {
            for (String option : options) {
                config.put(option, true);
            }
        }

        return config;
    }
}
```


Here is the output:

```json
[
    {
        "name": {
            "given": "John",
            "middle": "Edward",
            "surname": "Doe"
        },
        "age": 42,
        "isMarried": true,
        "address": {
            "street": "Main Street",
            "city": "New York",
            "zipCode": "10044",
            "country": "United States"
        },
        "phoneNumber": [
            "+1 (718) 111-1111",
            "+1 (718) 111-1112"
        ]
    }
]
```