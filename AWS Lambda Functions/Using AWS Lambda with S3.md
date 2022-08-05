Let’s take an example where a user is uploading an image on a website for resizing it.

-   First, the user creates a Lambda function.
-   The user uploads the code to the Lambda function.
-   Then, the user uploads the image from the website to the S3 bucket as an object.
-   After receiving the object, the S3 bucket triggers the Lambda function.
-   Then, the Lambda function does its job by resizing the image in the back-end and sends a successful completion email through SQS.

**The pseudo-code for the Lambda function:**

```
<code to resize image>

<once the image is resized, send the email for successful operation through SQS>
```

From this example, it is clear how AWS Lambda performs its tasks in the back-end.

Check the below diagram for a summary to it:  
![diagram for a summary](https://intellipaat.com/mediaFiles/2018/12/diagram-for-a-summary.png)

[[ AWS Lambda vs AWS EC2]]

