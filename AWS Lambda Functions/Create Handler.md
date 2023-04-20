Simply put, to invoke a lambda function, we need to specify a handler; there are 3 ways of creating a handler:

1.  Creating a custom _MethodHandler_
2.  Implementing the _RequestHandler_ interface
3.  Implementing the _RequestStreamHandler_ interface



https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/java-basic/src

#### Create a mvn project, take an emp object, print emp to json, a file with json, iterate it as java object and print after sorting

package handler;

import org.json.simple.JSONObject;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

public class TestJSonObjectJsonArray {
	public String handleTest() {
		JSONObject jsonObject = new JSONObject();
		jsonObject.put("College", College.collegeObject());
		return tojsonString(jsonObject);

	}

	// to pretty print the json
	public static String tojsonString(JSONObject jsonObj) {
		Gson gson = new GsonBuilder().setPrettyPrinting().create();
		String objectToString = jsonObj.toString();
		JsonElement je = JsonParser.parseString(objectToString);
		return gson.toJson(je);
	}

}
