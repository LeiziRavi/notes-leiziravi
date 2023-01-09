#### Data Communication:
- Data communication are the exchange of data between two nodes via some form of link (transmission medium) such as a cable.


#### Data Flow:
- Data is going to flow from one node to another node.
- There are three different types of flows:
	- Simplex
		- Sommunication is always unidirectional.
		- One device can transmit and the other device will receive.
		- Example: Keyboard, Traditional monitors
	- Half Duplex
		- Communication is in both directions but not at the same time.
		- If one device is sending, the other can only receive, and vice versa.
		- Example: Walkie-talkies
	- Full Duplex
		- Communication is in both directions simultaneously.
		- Device can send and receive at the same time.
		- Example: Telephone line


#### Protocols
- All communications schemes will have the following things in common:
	- Source or sender
	- Destination or receiver
	- Channel or media
- __Rules or protocols govern all methods  of communication__
- __Protocol=Rule__
- It is set of rule that govern data communication
- Protocol Determines:
	- __What__ is communicated?
	- __How__ it is communicated?
	- __When__ it is communicated?


#### Protocols - Human Communication
- Protocols are necessary for human communication and include:
	- An identified sender and receiver
	- Common language and grammar
	- Speed and timing of delivery
	- Confirmation or acknowledgment requirements


#### Protocols - Network Communication
- Protocols used in network communications also define:
	- Message encoding
	- Message formatting and encapsulation
	- Message timing
	- Message size
	- Message delivery options


#### Elements of A Protocol:
1. Message encoding
![[Message Encoding.png]]
2. Message formatting and encapsulation
	1. Both sender and receiver must mutually agree on certain formats which we call as formatting
	2. At the same time, when the receiver receives some data, it should identify who has send this data 
	3. We are going to add some information [i.e. we are going to encapsulate some information about the sender and the receiver] into data in order to identify the sender and the receiver.
3. Message timing
	1. Flow control
		1. Say sender is very fast and receiver is slow, hence receiver can handle the data flow, hence entire communication will be useless
	2.  Response timeout
4. Message size
	1. Human break long messages into smaller parts or sentences.
	2. Long messages must also be broken into smaller pieces to travel across a network.
5. Message delivery options
	1. There are three delivery options:
		1. Unicast
			1. One sender and one receiver
		2. Multicast
			1. if sender sends the data to a set of receivers but not to all
		3. Broadcast
			1. If sender sends the data to all the participants in the network






