
## Need for AWS Lambda

Suppose, a website is hosted on AWS EC2, in which currently 90–100 users are reading a blog and, in the back-end, the Admin User uploads 10 videos on the website for processing.  
![Need aws Lamda](https://intellipaat.com/mediaFiles/2018/12/Need-aws-Lamda.png)  
This increases the load on the server, which triggers the auto-scaling feature, and hence EC2 provisions more number of instances to meet this requirement—since hosting and back-end changes are both taking place in the same instance.

However, ==auto-scaling takes a long time to provision more instances, which eventually becomes a reason for slow actions on the website when the initial spike in the task is received==.  
![Need aws lamda website](https://intellipaat.com/mediaFiles/2018/12/Need-aws-lamda-website.png)  
This problem can be solved using distributed computing. In this, the website is hosted on one instance and the back-end code runs on another. While the users are reading a blog on the website, the Admin User can upload those 10 videos on the website.

This time, the website will forward the task of video processing to another instance. This makes the website resistant to video processing, and therefore website performance will not be impacted. However, ==video processing still takes a lot of time, when the load increases, because auto-scaling takes time on EC2==.  
![website system](https://intellipaat.com/mediaFiles/2018/12/website-system.png)Here, we need a **stateless system** to solve this problem, and AWS does exactly this with the launch of **AWS Lambda**!