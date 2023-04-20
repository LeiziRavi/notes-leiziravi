- Each container has its own file system, which is invisible to other containers.

__Experiment__:

```shell

# Two running containers
leiziravi@leiziravi:~$ sudo docker ps 
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS      NAMES
9f417e41c387   react-app   "docker-entrypoint.s…"   4 seconds ago    Up 2 seconds    3000/tcp   red-sky
26b421c88544   react-app   "docker-entrypoint.s…"   17 seconds ago   Up 15 seconds   3000/tcp   blue-sky

# start a shell session in one of the containers and write into a file
# close the session
leiziravi@leiziravi:~$ docker exec -it 9f4 sh
/app $ echo data > data.txt
/app $ exit

# Start a shell session with the other container and check for the file written in first container
leiziravi@leiziravi:~$ docker exec -it 26b sh
/app $ ls
README.md          node_modules       package.json       src
dockerfile         package-lock.json  public             yarn.lock
/app $ ls | grep data
/app $ 

# File is not available in the other container, 
# Hence, each container has a seperate file system.

```
- So if we delete the container, we also lose the data associated with that container.
- So it is advised to not store data on a container file system.
- That's what VOLUMES are for.