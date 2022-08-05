- If we go to http://localhost:3000 , we cannot access this application, becoz
	- PORT 3000 is publish on container not on the host so on the same machine we have multiple container, each container is listening on PORT 3000, but host itself is not listening on this port.
	- So this port is currently closed. There is no way to send traffic to localhost at this port, this is where we need to publish a port.


```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker ps
[sudo] password for leiziravi: 
CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS        PORTS                                                                                                                                  NAMES
3050527dada6   react-app                             "docker-entrypoint.s…"   16 hours ago   Up 16 hours   3000/tcp                                                                                                                               blue-sky
53f406ffa45b   react-app                             "docker-entrypoint.s…"   16 hours ago   Up 16 hours   3000/tcp                                                                                                                               festive_keller


```

#### To publish a container on a port
```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker run -d -p 3000:3000 --name c1 react-app
3c1c607b789b5761b9fefcfa72510584d1911d8dccc5dbd143d28f5966dd4b8b


```
```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS          PORTS                                                                                                                                  NAMES
3c1c607b789b   react-app                             "docker-entrypoint.s…"   46 seconds ago   Up 27 seconds   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp                                                                                              c1
3050527dada6   react-app                             "docker-entrypoint.s…"   16 hours ago     Up 16 hours     3000/tcp                                                                                                                               blue-sky
53f406ffa45b   react-app                             "docker-entrypoint.s…"   16 hours ago     Up 16 hours     3000/tcp  
```