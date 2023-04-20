==Running Python Application==
```bash
leiziravi  ~  docker -v
Docker version 20.10.17, build 100c701
leiziravi  ~  docker run -p 5000:5000 in28min/hello-world-python:0.0.1.RELEASE
Unable to find image 'in28min/hello-world-python:0.0.1.RELEASE' locally
0.0.1.RELEASE: Pulling from in28min/hello-world-python
21c83c524219: Pulling fs layer 
9a80d14c35bd: Pull complete 
0d32a27dde5a: Downloading [====================>                              ] 0d32a27dde5a: Downloading  20.76MB/22.57MB
0d32a27dde5a: Pull complete 
2cb80a514e07: Pull complete 
d5d3b19aaadd: Pull complete 
694c09e178f0: Pull complete 
2163a4c6fcc6: Pull complete 
26893ad78bb3: Pull complete 
Digest: sha256:a77f9165a81a3650f0211f823f7a5cdfdcb7b7e458cd193ea644ea10fb476fa2
Status: Downloaded newer image for in28min/hello-world-python:0.0.1.RELEASE
 * Serving Flask app 'launch' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 548-250-706
172.17.0.1 - - [16/Jan/2023 19:34:48] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [16/Jan/2023 19:34:49] "GET /favicon.ico HTTP/1.1" 404 -


```


__DOCKER__ - Simplify Deployment - Avoid Error Prone Manual Installations

With Docker:
- No details application we want to run
- No need to worry about which language the application is built with
- No need to worry about versions of language
- No need to know about the frameworks used to develop the application
- Or the softwares need to run the application


Only the developer needs to do is : __CREATE AN IMAGE__

==CTRL + C : TERMINATE CONTAINER==


==Running Java Application==

```bash
docker run -p 5000:5000 in28min/hello-world-java:0.0.1.RELEASE
```


==Running NodeJs Application==

```bash
leiziravi  ~  docker run -p 5000:5000 in28min/hello-world-nodejs:0.0.1.RELEASE
Unable to find image 'in28min/hello-world-nodejs:0.0.1.RELEASE' locally
0.0.1.RELEASE: Pulling from in28min/hello-world-nodejs
e7c96db7181b: Already exists 
e3b1e747cbd3: Pull complete 
017f53a1e6e8: Pull complete 
4cfcfaa362d1: Pull complete 
b6cd29cc2885: Pull complete 
b51cbf8d9088: Pull complete 
50b62877eafa: Pull complete 
Digest: sha256:0688621026b204e653b26d73f6a84af221ec92f1c4da93112f13a84ae16a112b
Status: Downloaded newer image for in28min/hello-world-nodejs:0.0.1.RELEASE
Ready on port 5000!

```


![[Response of JS application Run from Docker.png| 500x200]]



__Quick Tip for Windows 10 : Use 192.168.99.100 in URL instead of localhost__

If you are using **Window 10** and are using **docker toolbox**

=> Use **192.168.99.100** instead of **localhost**.

**Note:** If **192.168.99.100** does not work, you can find the IP by using the command `docker-machine ip`

**Reason**

**In Window 10** when using **docker toolbox** , docker is configured to use the default machine with IP 192.168.99.100