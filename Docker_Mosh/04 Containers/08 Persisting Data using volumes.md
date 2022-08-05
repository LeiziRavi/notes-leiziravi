- Volume is a storage outside of the containers.
- It can be directory in the host, or somewhere in the cloud

```shell
leiziravi@leiziravi:~$ sudo docker volume

Usage:  docker volume COMMAND

Manage volumes

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes

Run 'docker volume COMMAND --help' for more information on a command.
```


- Create a new volume
```shell
leiziravi@leiziravi:~$ sudo docker volume create app-data
app-data

```

- Inspect a volume
```shell
leiziravi@leiziravi:~$ sudo docker volume inspect app-data
[
    {
        "CreatedAt": "2022-05-14T14:55:46+05:30",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/app-data/_data",
        "Name": "app-data",
        "Options": {},
        "Scope": "local"
    }
]

# To create a volume in cloud platform, need to use specific drivers to that platform
# Mountpoint: This is where the directory has been created on the host.
# 

```
- Running an image with volume
```shell
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker run -d -p 5000:3000 -v app-data:/app/data react-app
ab554b8b6d0b3056b7f03fdb29a25d0b1f3546a7970eb1efed64db5fdcd12fb7

```
- Creating a file in the volume
```shell

leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker exec -it ab5 sh
/app $ cd data/
/app/data $ echo data > data.txt
/app/data $ exit

```

```shell
# Removing the container where the volume was created
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker rm -f ab5
ab5

# Starting a new container with samevolume mapping
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker run -d -p 5000:3000 -v app-data:/app/data react-app
612f1cc64f50effd5d8a951a61d34118f303fb8d408c813559f511f79f07f999

# Starting a shell session in running container to check on file created on previous container
leiziravi@leiziravi:~/work/Docker/react-app$ sudo docker exec -it 612 sh
/app $ ls
README.md          dockerfile         package-lock.json  public             yarn.lock
data               node_modules       package.json       src
/app $ ls data/
data.txt

# Though the container was removed, the volume and the data is still persistent.

```
__Volumes are perfect way to persist data in the containers because they have different life-cycles.__

- If we delete a container, the associated volume is not deleted. 
- Also, we can share volumes amongst multiple containers.
