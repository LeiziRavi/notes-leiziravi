https://cs.lmu.edu/~ray/notes/javanetexamples/ 

![[Pasted image 20220428003846.png]]

Discussion:

-   This code is just for illustration; you are unlikely to ever write anything so simple.
-   This does not handle multiple clients well; each client must wait until the previous client is completely served before it even gets accepted.
-   As in virtually all socket programs, a server socket _just listens_, and a different, “plain” socket communicates with the client.
-   The `ServerSocket.accept()` call is a BLOCKING CALL.
-   Socket communication is always with bytes; therefore sockets come with input streams and output streams. But by wrapping the socket’s output stream with a `PrintWriter`, we can specify strings to write, which Java will automatically convert (decode) to bytes.
-   Communication through sockets is always buffered. This means nothing is sent or received until the buffers fill up, _or_ you explicitly flush the buffer. The second argument to the `PrintWriter`, in this case `true` tells Java to flush automatically after every `println`.
-   We defined all sockets in a try-with-resources block so they will automatically close at the end of their block. No explicit `close` call is required.
-   After sending the datetime to the client, the try-block ends and the communication socket is closed, so in this case, closing the connection is initiated by the server.


Run the server:
```shell
$ javac DateServer.java && java DateServer
The date server is running...

```

To see that is running (you will need a different terminal window):

```shell
$ netstat -an | grep 59090
tcp46      0      0  *.59090                *.*                    LISTEN

```

Test the server with nc:
```shell
$ nc localhost 59090
Sat Feb 16 18:03:34 PST 2019
```

![[Pasted image 20220428004112.png]]


Discussion:

-   On the client side, the `Socket` constructor takes the IP address and port on the server. If the connect request is accepted, we get a socket object to communicate.
-   Our application is so simple that the client never writes to the server, it only reads. Because we are communicating with text, the simplest thing to do is to wrap the socket’s input stream in a `Scanner`. These are powerful and convenient. In our case we read a line of text from the server with `Scanner.nextLine`.

Test the client:

```shell

$ javac DateClient.java && java DateClient 127.0.0.1
Server response: Sat Feb 16 18:02:35 PST 2019

```
