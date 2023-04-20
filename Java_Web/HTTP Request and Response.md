HTTP: 

- It stands for Hypertext Trasnfer Protcol.
- Using this protocol the client send a request to the server and based on the request the server and the web browser repsond to the client.
- A http request contains:
	- A **method**. The method is a one-word command that tells the server what it should do with the resource. For example, the server could be asked to send the resource to the client.
	- The path component of the URL (i.e. URI) for the request. The path identifies the resource on the server.
	- The HTTP version number, showing the HTTP specification to which the client has tried to make the message comply.
	- Optional Header information (e.g. accept, cookies)


```shell
GET /software/htp/cics/index.html HTTP/1.1
```

After the client send the request, server processes the request and sends the response.

- A http response contains:
	- 



links:
1. https://www.ibm.com/docs/en/cics-ts/5.3?topic=concepts-components-url#dfhtl_uricomp