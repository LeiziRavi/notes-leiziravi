#### Switching 
- Switching in computer network helps in deciding the best route for data transmission if there are multiple paths in larger network.
- One-to-One connection.


#### Switching Techniques
![[switching techniques.png]]

1. __Circuit Switching__:
	- A dedicated path is established between the sender and the receiver
	- Before the data transfer, connection will be established first.
	- Example: Telephone Network
	- Three Phases in Circuit Switching:
		1. Connection establishment
		2. Data Transfer 
		3. Connection Disconnection


2. __Message Switching__:
	- Store and forward mechanism
	- Message is transferred as a complete unit and forwarded using store and forward mechanism at intermediary node
	- Not suited for streaming media and real-time applications

3. __Packet Swicthing__:
	- Internet is packet switching network
	- Message is broken into individual chunks called as packets
	- Each packet is sent individually
	- Each packet will have source and destination IP address with sequence number.
	- Sequence numbers will help the receiver to:
		- Reorder the packets
		- Detect missing packets and
		- Send acknowledgements
	- Two approaches to Packet Switching:
		1. Datagram Approach
			- Datagram Packet switching is also known as connection-less switching.
			- Each independent entity is called as datagram
			- Datagrams contain destination information and the intermediary devices uses this information to forward datagrams to right destination.
			- In Datagram Packet Switching approach, the path is not fixed.
			- Intermediate nodes takes the routing decisions to forward the packets 
		2. Virtual circuit approach
			- Virtual Circuit Switching is also known as connection-oriented switching.
			- In the case of Virtual circuit switching, a preplanned route is established before the messages are sent.
			- Call request and call accept packets are used to establish the connection between sender and receiver.
			- In this approach, the path is fixed for the duration of a logical connection.