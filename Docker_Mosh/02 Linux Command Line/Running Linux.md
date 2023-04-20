```shell
docker pull ubuntu
```

but the shortcut is:

```shell
docker run ubuntu
```

- If we have this image locally, docker  will start a container with this image otherwise it is going to pull the image behind the scene and then start a container.

```shell
docker ps

# list of running processes or running containers
```

- To start a container and interact with it, 

```shell
docker run -it ubuntu

# -it for interactive
```

