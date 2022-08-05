![[Lambda Execution Environment.png]]
A function is executed, or invoked, whenever the invoke command of the AWS Lambda API is called. 
This happens at the following times: 
- When a function is triggered by an event source 
- When you use the test harness in the web console 
- When you call the Lambda API invoke command yourself, typically via the CLI or SDK, from your own code or scripts.

- Invoking a function for the first time will start the following chain of activity that will end in your code being executed.

1. First, the Lambda service will create a host Linux environment—a lightweight micro-virtual machine. You typically won’t need to worry about the precise nature of what type of environment it is (which kernel, what distribution, etc.), but if you do care, Amazon makes that information public. But don’t rely on it staying constant—Amazon can and does make frequent changes to the OS of Lambda functions, often for your own benefit, including automatic security patches. 
2. Once the host environment has been created, then Lambda will start a language run‐ time within it—in our case a Java virtual machine. 
3. The JVM version will always be Java 8 or Java 11. ==You must supply Lambda with code compatible with the version of Java that you choose==. The JVM is started with a set of environment flags that we can’t change.
4. You may have noticed when we wrote our code that there was no “main” method— the top-level Java application is Amazon’s own Java application server, which we’ll refer to as the Lambda Java Runtime; that’s the next component to be started. The runtime is responsible for top-level error handling, logging, and more. Of course, the Lambda Java Runtime’s primary concern is executing our code. 
5. The final steps of the invocation chain are (a) to load our Java classes and (b) to call the handler method that we specified during deployment.



s3 bucket --> file upload --> read from the code


  

AmazonS3Client s3Client = (AmazonS3Client) AmazonS3ClientBuilder.standard().build();  
S3Object s3Object = s3Client.getObject(Constants.CONFIGURATION_BUCKET, "InquiryMapping.json");  
LinkedHashMap<String, LinkedHashMap> config = new ObjectMapper().readValue(s3Object.getObjectContent(), LinkedHashMap.class);