Although AWS Lambda offers so many benefits, we might face a few limitations while working with AWS Lambda, due to its various characteristics w.r.t. its hardware and its architecture. 
Some of these limitations are listed below:

-   The maximum execution duration per request is set to 300 seconds (15 minutes)
-   In the case of hardware, the maximum disk space provided is 512 MB for the runtime environment, which is very less
-   Its memory volume varies from 128 MB to 1,536 MB
-   The event request body cannot exceed more than 128 KB
-   Its code execution timeout is only 5 minutes
-   Lambda functions write their logs only to CloudWatch, which is the only tool available in order to monitor or troubleshoot our functions

These limitations of AWS Lambda basically exist to ensure that the services are used as intended.