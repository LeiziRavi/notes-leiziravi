
Concept of layers in docker:
- An image is essentially a collection of layers
- A layer can be thought of a file system which only include modified files.
- So, when docker tries to build an image for us, it executes each of the instructions in Dockerfile and creates a new layer. That layer only includes the files that are modified as the result of that instruction.
- To view layers:
	```shell
	docker history react-app
``` 




```dockerfile
#layer1 , now FROM layer will have it's own extra layers for linux
FROM node:14.16.0-alpine3.13 
#layer2
RUN addgroup app && adduser -S -G app app  
USER app
WORKDIR /app 
# here, COPY . . is a special instruction and with this instruction Docker
# cannot tell if anything is changed or not
# so it has to look at the ocntents of the files as well and that means
# even if we make a tiny change in our application, if we write one extra 
# line of code docker cannot reuse this layer from cache, 
# it has to rebuild it. This is where the problem happens
# once the layer is rebuilt, all the following layers need to be rebuild as well. 
# so the docker has to install all the dependencies from npm
COPY . . 
RUN npm install
ENV API_URL=http://api.myapp.com
EXPOSE 3000
CMD ["npm","start"]

```

- So to optimize our build, we have to seperate all the installation of third-party dependecies from copying the installtion files.

```dockerfile
FROM node:14.16.0-alpine3.13
RUN addgroup app && adduser -S -G app app 
USER app
WORKDIR /app
COPY package*.json ./
RUN ["npm","install"]
COPY . .
ENV API_URL=http://api.myapp.com
EXPOSE 3000
CMD ["npm","start"]

```

>__NOTE__:
	To optimize the build, we should organize the dockerfile such that the instructions that don't change frequently should be on the top and the instructions or files that change frequently should be down to bottom.