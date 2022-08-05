- Whenever we build an image or pull an image from docker hub, the docker uses _latest_ tag, 
- __"_latest_"__ tag is just a label, there is nothing special about it, it doesn't necessarily mean that this is the latest version of the image.
- use of __"_latest_"__ tag is fine in development but __do not use it in production__.
- As it will always show latest, we will have difficulties while troubleshooting issues i.e. what version we are using?



#### Method 1 : Tagging while building an image
```
docker build -t react-app:1 .
```

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker images
REPOSITORY                    TAG                  IMAGE ID       CREATED          SIZE
react-app                     1                    97882faef04f   28 minutes ago   298MB
react-app                     latest               97882faef04f   28 minutes ago   298MB
node                          alpine               d94913fe64df   9 days ago       171MB
ubuntu                        latest               d2e4e1f51132   13 days ago      77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.30              1312ccd2422d   3 months ago     1.14GB
node                          14.16.0-alpine3.13   50bfd284aa0d   13 months ago    117MB


```

- To remove a tag:

```shell
docker image remove react-app:1
```

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker image remove react-app:1
Untagged: react-app:1
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker images
REPOSITORY                    TAG                  IMAGE ID       CREATED          SIZE
react-app                     latest               97882faef04f   29 minutes ago   298MB
node                          alpine               d94913fe64df   9 days ago       171MB
ubuntu                        latest               d2e4e1f51132   13 days ago      77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.30              1312ccd2422d   3 months ago     1.14GB
node                          14.16.0-alpine3.13   50bfd284aa0d   13 months ago    117MB
```


#### Method 2: Tagging an existing image

```shell
docker image tag react-app:latest react-app:1
# we can use full image name or image id folloing with the image tag

```

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker image tag react-app:latest react-app:1
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker images
REPOSITORY                    TAG                  IMAGE ID       CREATED          SIZE
react-app                     1                    97882faef04f   35 minutes ago   298MB
react-app                     latest               97882faef04f   35 minutes ago   298MB
node                          alpine               d94913fe64df   9 days ago       171MB
ubuntu                        latest               d2e4e1f51132   13 days ago      77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.30              1312ccd2422d   3 months ago     1.14GB
node                          14.16.0-alpine3.13   50bfd284aa0d   13 months ago    117MB

```

#### "latest" doesn't necessarily always point to the latest build. We explicitly need to apply latest tag to latest image-build.