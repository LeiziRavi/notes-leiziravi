# Optimizing Cold Starts

There are two main tactics you can use when battling cold starts: minimizing the duration of the cold start (meaning cutting down the latency of the cold start itself) and minimizing the number of times cold starts occur. The former is done by using common programming patterns and common sense, while the latter is achieved with a technique called function warming. Let’s explain in more detail.

## Minimizing the Duration of Cold Starts

You can shave down the time impact of cold starts by writing functions using interpreted languages. Cold start latency with [Node.js](https://docs.epsagon.com/docs/nodejs) or [Python](https://docs.epsagon.com/docs/python) is well under a second. A compiled language like [Go](https://epsagon.com/blog/getting-started-with-aws-lambda-and-go/) is another example of low cold start latency. Another easy step is to choose higher memory settings for your functions. This also gives your functions more CPU power. However, the most important consideration is to avoid VPCs. VPCs have to create ENIs, which take well over 10 seconds to initialize. Please, don’t put your functions in a VPC. Just don’t!

## Minimizing the Frequency of Cold Starts

You can reduce the number of cold starts that occur in the first place with function warming. This is the act of sending scheduled ping events to your functions to keep them alive and idle, ready to serve requests. With [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html), triggering the functions periodically to always have a fixed number of AWS Lambda instances alive is simple. Just set up a [periodic cron job](https://read.acloud.guru/how-to-keep-your-lambda-functions-warm-9d7e1aa6e2f0) to trigger your function every 5-15 minutes, and rest assured, it will always be idle.

Once again, this raises the question: How do you handle concurrent cold starts? Luckily, there are a few modules and plugins to use. If you’re a Node.js developer, [Lambda Warmer](https://www.npmjs.com/package/lambda-warmer) will hit home. [Jeremy Daly](https://twitter.com/jeremy_daly), CTO of AlertMe.news, discussed Lambda Warmer on our [serverless and observability webinar](https://epsagon.com/blog/serverless-monitoring-in-practice-webinar/). It lets you warm concurrent functions, and even choose the level of concurrency you want. And, it works with both the Serverless Framework and AWS SAM. The Serverless Framework has another plugin you can use, called [Serverless WARM-Up Plugin](https://github.com/FidelLimited/serverless-plugin-warmup). But sadly, it doesn’t support concurrent function warming.

In order to correctly warm your functions, you should follow a few simple steps:

-   Don’t invoke the function more often than once every five minutes.
-   Invoke the function directly with Amazon CloudWatch Events.
-   Pass in a test payload when running the warming.
-   Create handler logic that doesn’t run all function logic when it is running the warming.

Here’s what a handler function would look like with warmer logic included:

```js
const warmer = require('lambda-warmer')
exports.handler = async (event) => {
	// if a warming event
	if (await warmer(event)) return 'warmed'
	// else proceed with handler logic
	return 'Hello from Lambda'
}
```
The event trigger configuration with the Serverless Framework would only require you to add a few lines of YAML:

```yaml
myFunction:
name: myFunction
handler: myFunction.handler
events:
	- schedule:
		name: warmer-schedule-name
		rate: rate(5 minutes)
		enabled: true
		input:
			warmer: true
			concurrency: 1
```
By using this warmer, you can safely keep as many AWS Lambda instances running as you want, including copies of the same function if you are expecting concurrent requests. So, say goodbye to cold starts.