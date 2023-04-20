- So we have few images and containers on our machine

```shell
Leiziravi@leiziravi:~/work/Docker/react-app$  docker images
REPOSITORY                    TAG                  IMAGE ID       CREATED         SIZE
react-app                     latest               35075ae69bd5   20 hours ago    298MB
<none>                        <none>               97882faef04f   2 days ago      298MB
node                          alpine               d94913fe64df   11 days ago     171MB
ubuntu                        latest               d2e4e1f51132   2 weeks ago     77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.30              1312ccd2422d   3 months ago    1.14GB
node                          14.16.0-alpine3.13   50bfd284aa0d   13 months ago   117MB


leiziravi@leiziravi:~/work/Docker/react-app$ docker ps -a
CONTAINER ID   IMAGE       COMMAND                  CREATED        STATUS                    PORTS                                       NAMES
b6117584af56   react-app   "docker-entrypoint.s…"   18 hours ago   Exited (1) 18 hours ago                                               naughty_mendel
ed48d732e652   react-app   "docker-entrypoint.s…"   18 hours ago   Exited (1) 18 hours ago                                               magical_faraday
4b4ddac49a48   react-app   "docker-entrypoint.s…"   18 hours ago   Up 18 hours               0.0.0.0:5001->3000/tcp, :::5001->3000/tcp   vigorous_jones
b6f8f5f698c7   react-app   "docker-entrypoint.s…"   18 hours ago   Exited (1) 18 hours ago                                               heuristic_easley


leiziravi@leiziravi:~/work/Docker/react-app$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED        STATUS        PORTS                                       NAMES
4b4ddac49a48   react-app   "docker-entrypoint.s…"   18 hours ago   Up 18 hours   0.0.0.0:5001->3000/tcp, :::5001->3000/tcp   vigorous_jones

```

### docker image

```shell

# docker image ls gives all the information related to the docker image
leiziravi@leiziravi:~/work/Docker/react-app$ docker image ls
REPOSITORY                    TAG                  IMAGE ID       CREATED         SIZE
react-app                     latest               35075ae69bd5   20 hours ago    298MB
<none>                        <none>               97882faef04f   2 days ago      298MB
node                          alpine               d94913fe64df   11 days ago     171MB
ubuntu                        latest               d2e4e1f51132   2 weeks ago     77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.30              1312ccd2422d   3 months ago    1.14GB
node                          14.16.0-alpine3.13   50bfd284aa0d   13 months ago   117MB


# docker image ls -q : gives only the images Id list
leiziravi@leiziravi:~/work/Docker/react-app$ docker image ls -q
35075ae69bd5
97882faef04f
d94913fe64df
d2e4e1f51132
1312ccd2422d
50bfd284aa0d

```


### To remove all the images 

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ docker image rm $(docker image ls -q)

```

#### But the above command will result in a n error, since some of these images are already in use in running containers or stooped containers

```shell
Error response from daemon: conflict: unable to delete 35075ae69bd5 (cannot be forced) - image is being used by running container 4b4ddac49a48

Error response from daemon: conflict: unable to delete 50bfd284aa0d (cannot be forced) - image has dependent child images

```

#### So, we should always remove the container first.

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ docker container rm -f $(docker container ls -aq)
b6117584af56
ed48d732e652
4b4ddac49a48
b6f8f5f698c7

# -f : to force remove running containers
# -a : for stooped containers
# -q : for list of runing conatiner Ids
```


#### Everything is deleted.

```shell
# No running containers
leiziravi@leiziravi:~/work/Docker/react-app$ docker ps 
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# No stopped containers
leiziravi@leiziravi:~/work/Docker/react-app$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# No docker images
leiziravi@leiziravi:~/work/Docker/react-app$ docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
leiziravi@leiziravi:~/work/Docker/react-app$ 

```



#### But there is shortcut to this process as well.

##### -> Using Docker Desktop
