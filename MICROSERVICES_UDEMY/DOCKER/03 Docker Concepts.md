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


==in28min/hello-world-nodejs:0.0.1.RELEASE==
- This is a path to the docker image, which is stored on a Docker Registry called [[Docker Hub]]. 
- in28min/hello-world-nodejs : Repository
- 0.0.1.RELEASE : Specific release


==unable to find image 'in28min/hello-world-nodejs:0.0.1.RELEASE' locally==
- Docker is checking if the image is present locally
- and it is unable to find one locally

==0.0.1.RELEASE: Pulling from in28min/hello-world-nodejs==
- Connecting Docker Hub, and pulling the image from this repo to the local machine
- Once it downloads, it runs the image.
- __*The running version of the image is called a container.*__
- An image in itself is static.
- Even after it is downloded, it is just set of bytes that are downloded to the machine.
- When an image is running, it is called a container. 
- For one image we can have a lot of containers running.

==-p 5000:5000==
- Whenever we run any image, it is part of an internal Docker network, called Bridge Network.
- So by default all conatiners run inside the Bridge Network.
- We won't be able to access the container, unless the port is exposed outside.
- Here we are exposing the container port 5000 and mapping it to a host port (i.e. a port on the local machine) 5000.
- And the option which is used to enable this is "-p" (which is short for --publish)
- 