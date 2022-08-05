- Docker uses a client server architecture
- It has a client component which talks to the server using a RestFul API.
- Server also called Docker Engine sits at the background and takes care of the building and running docker containers.


 ![[Docker Architecture.png | 600 x 250]]

- Technically a container is just a process, like other processes running on the computer.

![[ Container is just another process.png | 600 x 250]]

- As we know, like VMs a container do not contain a full-blown operating system, instead all container on a host share the operating system of the host. 
	- More accurately all those containers share the kernel of the host.
	- A kernel manages applications and hardware resources like memory and cpu.
	- Every operating system has its own kernel or engine, and these kernels have different apis. 
	- That is the reason we can npt run a windows application on linux. Becoz under the hood this application is to talk to the kernel of the underlying os.
	- On linux machine, we can only run linux containers.
	- However on a windows machine, we can run windows as well as linux containers. Becoz windows 10 not shipped with a custom build linux kernel. this is in addition to the windows kernel that always been in windows.
	- Mac kernel do not have native support for containers. So Docker on Mac uses a lightweight linux vm to run linux containers.