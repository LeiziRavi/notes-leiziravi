## What is Provisioned Concurrency and How Can it Solve Cold Starts?
Knowing that the major reason behind cold starts is the time taken to initialize the computing worker nodes, AWS’ Provisioned Concurrency solution is quite simple. Already have those worker nodes initialized!

The concept here is that you can now decide how many of these worker nodes you would like to keep initialized for your time-sensitive serverless applications. These worker nodes will reside in a frozen state with your code downloaded and underlying container infrastructure all set. Hence technically still not using up any resources, the benefit here is a guaranteed response time of almost double-digit milliseconds. This is a considerable improvement compared to the latency creeping into the seconds if not minutes with the .NET example whose cold start durations are illustrated above.

That means, depending on the number of concurrent worker nodes you have, invocations shall be routed to provisioned worker nodes before on-demand worker nodes, thus avoiding cold starts due to the need for initialization. It would thus be wise to provision a higher number of worker nodes for expected spikes in traffic.


## How to Turn On Provisioned Concurrency

The steps below explain how you can configure Provisioned Concurrency for your Lambda functions using the AWS Management Console.

1.  In the AWS Lambda console, choose an existing Lambda function.
2.  In the **Actions** drop-down menu, choose the **Publish new version** option. This will let you apply settings to an alias or a published version of a function.

![](https://res.cloudinary.com/lumigo-production/w_557,h_118,c_fit/dpr_auto,w_auto,q_auto:eco/wp-website/2020/09/cold-starts-2.png)

Image Source: [AWS](https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/)

3.  You can add a description for the version, but this is optional. When done, choose the **Publish** option.
4.  In the **Actions** drop-down menu, choose the **Create alias** option. For each alias, enter a name.
5.  In the **Version** drop-down menu, and choose **1**, and then choose **Create**.

![](https://res.cloudinary.com/lumigo-production/w_503,h_221,c_fit/dpr_auto,w_auto,q_auto:eco/wp-website/2020/09/cold-starts-3.png)

Image Source: [AWS](https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/)

6.  Find the **Concurrency** card and then choose the **Add** option.
7.  Choose the **Alias** radio button for **Qualifier Type**, and then choose the function alias you selected previously in the **Alias** drop-down menu. Define the required value for **Provisioned Concurrency** – the number specifies the number of function instances that will run continuously. Choose **Save**.

**Warning – additional costs**: provisioned concurrency is billed in addition to regular invocation costs for AWS Lambda. You pay for provisioned concurrency as if additional instances of your function were invoked and running on a continuous basis.

8.  After you complete step 7, go to the Lambda console. The **Provisioned Concurrency** card should display the **In progress** status.

The initialization process will be complete after several minutes, and then you can use the published alias of your function with the Provisioned Concurrency feature.

![](https://res.cloudinary.com/lumigo-production/w_503,h_230,c_fit/dpr_auto,w_auto,q_auto:eco/wp-website/2020/09/cold-starts-4.png)

Image Source: [AWS](https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/)

The above steps apply to the AWS Management Console. You can also use AWS CloudFormation, the AWS CLI, and AWS SDK to modify these settings.