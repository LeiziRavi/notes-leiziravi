```shell
useradd -m john

# -m : creating home directory
```

- To check the creation of new user:

```shell
cat /etc/passwd
```

- To modify the user to use bash shell
```shell
usermod -s /bin/bash /john
```

- Passwords are saved in a encrypted format in a file
```shell
cat /etc/shadow
```

- To login as another user 
```shell
docker exec -it -u {username} {container_id} bash
```

- Difference between useradd & adduser:
	- __useradd__ was the original api that was build, but __adduser__ is a perlscript that is more interactive and uses useradd under the hood. 