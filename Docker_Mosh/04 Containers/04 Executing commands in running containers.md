- When we start a container, its execute the default command specified in the Dockerfile, 
- What If we want to execute any command in a running container later on.
- Lets say we want to troubleshoot something and we want to look at file system of that container.

 `docker exec`
- with this we can execute a command in a running container.

> Difference between exec and run?
> -> With run we start a new container, and run a command.
> -> With exec, we execute a command in a running container.