## What Is an AWS Lambda Cold Start?

![[Pasted image 20220603162212.png]]

An AWS Lambda cold start occurs when a new instance of a function needs to be created in response to an invocation. When [function instances](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html) are created in Lambda, each instance only persists for a limited period, usually between 10 to 15 minutes. Each time the function is called this timer is reset. However, if it is not called before the time runs out, the container is terminated.

When a function is invoked and there are either no function containers running or not enough to handle the current requests, a new instance is made. The time it takes to create this instance, transfer function code, import dependencies, and deploy the instance make up the cold start time. 

Cold starts are a significant challenge in serverless architectures because they can create a noticeable lag for users. Considering user demand for instant gratification, this lag can seriously harm the quality and competitiveness of applications.


#### What Factors Contribute to Cold Start Times?
- Languages
	- The language and frameworks you are using play a large role in determining how fast your instances start up. 
	- In general, compiled languages are going to start up faster than interpreted but this isn’t always the case. 
	- For example, Go and Python both initialize faster than C# or Java. Meanwhile .NET is one of the slowest languages since it requires translating assemblies.
- Number of dependencies
	- When you initialize a function, all the dependencies you call in the function are imported. 
	- If you are using many libraries, each library you include adds more time. 
	- While this can’t be avoided for some functions, such as for machine learning, you should try to reduce dependencies wherever possible.
- Function chains
	- Function chains involve functions invoking other functions. 
	- When this occurs, any cold starts are transferred and accumulated down the line. 
	- During this chain any time functions are left waiting for a response is time you are charged for. 
	- Additionally, if your chain is excessively long or your cold start times high, your functions may time out.
- Virtual private clouds (VPC)
	- VPCs can help you keep your network and functions more secure by isolating traffic and enabling stricter controls. 
	- However, this creates an issue when functions try to communicate with outside components. 
	- If a function requires external access an Elastic Network Interface (ENI) must be created. 
	- This ENI creates an externally facing IP address which is attached to the function for request response traffic. 
	- Each time these addresses are added, it can take up to 10 seconds to set up, meaning 10 extra seconds of cold start time.


## Ways to Reduce the Impact of Lambda Cold Starts

### **Allocate more memory**

One way to reduce your start up times is to allocate more memory to your functions. Lambda resources scale linearly with more memory granting more CPU. More CPU means your initialization is processed faster, reducing cold start times. 

If you use this method just keep in mind that the resources you allocate determine the cost of your functions. For example, if you scale a 128MB function to the max size (3.8GB) you’ll see a cost increase of 25x. 

Depending on the amount of traffic your functions see this could be significant or a fair trade off. For example, a low traffic service with short calls may only see an increase of a dollar or two. In contrast, a high traffic service with longer calls could see increases in the tens of thousands.


### Use a basic HTTP client
Included in the AWS SDK are many HTTP client libraries that you can use to make SDK calls. These libraries add a lot of functionality, like connection pooling, that is great for stateful scenarios but less useful for stateless ones (i.e. Lambda).

Most Lambda functions require a handful of calls at most with results quickly returned to the client. Additionally, Lambda functions can only respond to a single request at a time, making multiple HTTP connections useless most of the time. 

Unless you have a good reason to use these libraries, you are better off sticking to the built-in Java HTTP client. Doing so reduces your dependencies, your complexity, and your cold start times.


### Preload dependencies
Whenever your function is invoked, dependencies are imported as part of the function. If you have large dependencies, or many, this can take a significant amount of time. However, you can also important dependencies outside your function and store them in the function instance for future invocations. This is accomplished with [handler functions](https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide/), used as a go between for invoking services and the function. 

Storing dependencies in the instance itself doesn’t eliminate cold start time. However, it can help offset start time by enabling future invocations to run faster and reduce your costs. This is because dependencies are already loaded, and can be referenced by the function immediately which reduces total run time and thus cost.





[[Cold Start Links]]