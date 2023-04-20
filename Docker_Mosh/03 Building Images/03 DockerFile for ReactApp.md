- A dcoker file contains instructions forbuilding an image.
- Options available:
	- __FROM__ - for specifying the base image
		- so we take that base image which contains the files and directories and then we build on top of it.
	- __WORKDIR__ - to specify the working directory
		- Once we use this command all the following commands will be executed in the current working directory.
	- __COPY__ - To copy files and directories
	- __ADD__ - has same synatx as COPY but have two extra features
		- use ADD only when we need these features i.e.
			- To add files from a url
			- To uncompress a compressed file
	- __RUN__ - For executing operating system commands
	- __ENV__- For setting environment variables
		- to check env in a linux system
			- printenv
			- printenv {environment_variable_name}
	- __EXPOSE__ - For telling docker that our container is starting on a given port
	- __USER__ - For specifying the user who should run the application typically should be a user with limited privilages
	- __CMD__ - for specifying the command that should be executed when we start a container 
	- __ENTRYPOINT__  




```dockerfile
FROM node:14.16.0-alpine3.13
WORKDIR /app
COPY . .
RUN npm install
ENV API_URL=http://api.myapp.com
EXPOSE 3000
RUN addgroup app && addgroup -S -G app app 
USER app
CMD ["npm","start"]

```

> 
> Building this image takes a long time due to npm install, installing the dependencies, we excluded the node_modules directory using .dockerignore for faster builds. But our builds are still slow, because everytime we build this image all the dependencies needs to be installed. 
> 


```dockerfile
FROM node:14.16.0-alpine3.13
RUN addgroup app && addgroup -S -G app app 
USER app
WORKDIR /app
COPY . . 
RUN npm install
ENV API_URL=http://api.myapp.com
EXPOSE 3000
CMD ["npm","start"]

```

- Difference between __RUN__ and __CMD__:
	- Run instruction is a built time instruction, so this is executed at the time of building the image.
	- eg. RUN npm install : so at the time of building we are installing the dependencies and these dependencies are stored in the image.
	- In contrast, CMD is a runtime instruction, so it is executed when starting a container.

	 Two forms:
	 1. __Shell form__  : Docker will execute this command in a seperate shell, i.e. why the name
		- CMD npm start
	 2. __Execute form__ : Common best practice is to use the Exec form, becoz with this we can execute this command directly and there is no need to spin up another shell process, also this makes it easier and faster to clean up resources when we stop containers, ___so always use Execute form.__
		 - CMD ["npm","start"]



- Difference between __CMD__ and __ENTRYPOINT__
	- We can always overwrite the default CMD, when starting a container.
	i.e. 
```shell
		docker run react-app echo hello

		# this will override CMD ["npm","start"]
```

- We cannot easily override the ENTRYPOINT when starting a container. To do that we need to use __--entrypoint__ option.
- Only use entrypoint when we know for sure this is the program that should be executed whenever you start a container.
- In contrast, with CMD we have more flexibility, we can always override this.

