- Head over to https://hub.docker.com/
- Create or login to hub account
- Create a Repository
	- can have multiple images with different tags

![[Create Repository.png]]

![[Repo name.png]]

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker images
REPOSITORY                    TAG                  IMAGE ID       CREATED          SIZE
react-app                     1                    97882faef04f   35 minutes ago   298MB
react-app                     latest               97882faef04f   35 minutes ago   298MB
node                          alpine               d94913fe64df   9 days ago       171MB
ubuntu                        latest               d2e4e1f51132   13 days ago      77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.30              1312ccd2422d   3 months ago     1.14GB
node                          14.16.0-alpine3.13   50bfd284aa0d   13 months ago    117MB

```

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker image tag 978 leiziravi/react-app:2
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker images
REPOSITORY                    TAG                  IMAGE ID       CREATED          SIZE
leiziravi/react-app           2                    97882faef04f   44 minutes ago   298MB
react-app                     1                    97882faef04f   44 minutes ago   298MB
react-app                     latest               97882faef04f   44 minutes ago   298MB
node                          alpine               d94913fe64df   9 days ago       171MB
ubuntu                        latest               d2e4e1f51132   13 days ago      77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.30              1312ccd2422d   3 months ago     1.14GB
node                          14.16.0-alpine3.13   50bfd284aa0d   13 months ago    117MB

```


```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: leiziravi
Password: 
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

```

```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker push leiziravi/react-app:2
The push refers to repository [docker.io/leiziravi/react-app]
f3ac962fa1a6: Pushed 
53b2538c7e77: Pushed 
d46d7d23ccc3: Pushed 
9efba758dbe7: Pushed 
a3f58f1f5b87: Pushed 
798e08027938: Mounted from library/node 
33cef85d9393: Mounted from library/node 
bcc9629c254f: Mounted from library/node 
8ea3b23f387b: Mounted from library/node 
2: digest: sha256:84beeb80c3d1528fb08a0a748d76033eb2ccdc56fb312fe3640c6ff8febd2fba size: 2205

```

![[Pushed image.png]]