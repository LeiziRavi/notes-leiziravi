- Sometimes we need to copy files from the host and a container.
- Ex. let say we have log file in our container, and we want to bring it to the host and analyse it.

```shell

# start a container and a shell session for it.
# create a log.txt file on the container.
leiziravi@leiziravi:~/work/Docker/react-app$ docker exec -it 612 sh 
/app $ echo hello > log.txt
/app $ ls
README.md          dockerfile         node_modules       package.json       src
data               log.txt            package-lock.json  public             yarn.lock
/app $ exit

# Use cp to copy file from docker container to the host machine
# docker cp {container_id/name}:{fully-qualified-path-for-source-file-on-container} {destination-file-path}
leiziravi@leiziravi:~/work/Docker/react-app$ docker cp 612f1cc64f50:/app/log.txt .
leiziravi@leiziravi:~/work/Docker/react-app$ ls
dockerfile  log.txt  package.json  package-lock.json  public  README.md  src  yarn.lock

# log.txt is copied to the host machine
```

#### Copy a file from the host to container

```shell
# Create a file on the host machine
leiziravi@leiziravi:~/work/Docker/react-app$ echo hello > secret.txt
leiziravi@leiziravi:~/work/Docker/react-app$ ls
dockerfile  log.txt  package.json  package-lock.json  public  README.md  secret.txt  src  yarn.lock

# Copy using cp command from machine to container
leiziravi@leiziravi:~/work/Docker/react-app$ docker cp secret.txt 612f1cc64f50:/app
leiziravi@leiziravi:~/work/Docker/react-app$ docker exec -it 612f1cc64f50 sh
/app $ ls -1
README.md
data
dockerfile
log.txt
node_modules
package-lock.json
package.json
public
secret.txt
src
yarn.lock


# File copied from host machine to the container.



```