```shell
mkdir hello-docker
```

```shell
cd hello-docker
```


- Open it in vscode or preferred code editor

```shell
code .
```


- add a new file

```js
//app.js

console.log("Hello Docker!");

```


__INSTRUCTIONS For deplying the program:__

- Start with an OS
- Install Node i.e. an execution environment for js codes
- Copy app files
- Run  node app.js

```shell
docker build -t hello-docker .
```

```shell
docker image ls
```

```shell
docker run hello-docker
```

```dockerfile
FROM node:alpine
COPY . /app
WORKDIR /app
CMD node app.js
```

