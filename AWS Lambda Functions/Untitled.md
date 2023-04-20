AmazonS3Client s3Client = (AmazonS3Client) AmazonS3ClientBuilder.standard().build();  
S3Object s3Object = s3Client.getObject(Constants.CONFIGURATION_BUCKET, "InquiryMapping.json");  
LinkedHashMap<String, LinkedHashMap> config = new ObjectMapper().readValue(s3Object.getObjectContent(), LinkedHashMap.class);




//		schema for including headers
//		CsvSchema schema = CsvSchema.emptySchema().withHeader();

//		MappingIterator<Map<String, String>> iterator = mapper.reader(Map.class).with(schema).readValues(stream);

arn:aws:lambda:ap-south-1:349519039469:function:apiPostLambda





```java
	@Override
	public String handleRequest(Map<String, Object> input, Context context) {
		Gson gson = new Gson();
		AmazonS3Client s3Client = (AmazonS3Client) AmazonS3ClientBuilder.standard().build();
		
		ObjectMapper mapper = new ObjectMapper();

		S3Object s3Object = s3Client.getObject(BUCKET_NAME, DEST_FILE_NAME);
		S3ObjectInputStream objectData = s3Object.getObjectContent();

		LinkedHashMap<String, LinkedHashMap> config = null;
		try {
			config = mapper.readValue(objectData,LinkedHashMap.class);
//			config = mapper.reader(LinkedHashMap.class).with(schema).readValues(s3Object.getObjectContent());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return gson.toJson(config,LinkedHashMap.class);
	}
```



https://kodejava.org/how-do-i-convert-csv-to-json-string-using-jackson



![[Pasted image 20220531165721.png]]


	<build>
		<plugins>
			<plugin>
				<artifactId>maven-shade-plugin</artifactId>
				<version>3.2.1</version>
				<executions>
					<execution>
						<phase>package</phase>
						<goals>
							<goal>shade</goal>
						</goals>
					</execution>
				</executions>
				<configuration>
					<finalName>lambda</finalName>
				</configuration>
			</plugin>
		</plugins>
	</build>






<dependency>  
<groupId>javax.validation</groupId>  
<artifactId>validation-api</artifactId>  
<version>2.0.1.Final</version>  
</dependency>  
  
<dependency>  
<groupId>org.hibernate.validator</groupId>  
<artifactId>hibernate-validator</artifactId>  
<version>6.0.13.Final</version>  
</dependency>  
  
<dependency>  
<groupId>org.glassfish</groupId>  
<artifactId>javax.el</artifactId>  
<version>3.0.0</version>  
</dependency>

<dependency>  
<groupId>javax.xml.bind</groupId>  
<artifactId>jaxb-api</artifactId>  
<version>2.3.0</version>  
</dependency>



ValidatorFactory factory = Validation.buildDefaultValidatorFactory();  
Validator validator = factory.getValidator();

validator.validate(object);


List Validator
