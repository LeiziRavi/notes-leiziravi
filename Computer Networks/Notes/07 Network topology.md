#### Network Topology
- It is the arrangement of nodes of a computer network.
- Topology=Layout
- Can be viewed as:
	- Physical Topology: Placement of various nodes
	- Logical topology : Deals with the data flow in the network


#### Types of topologies:
- __Bus__
		- Alll data transmitted between nodes in the network is transmitted over this ==common transmission medium== and is able to be received by all nodes in the network simultaneously.
		- A signal containing the address of the intended receiving machine travels from a source machinein ==both directions== to all machines connected to the bus until it finds the intended recipient.
		- ![[Bus topology.png]]
		
| Advantages                           | Disadvantages                     |
	| ------------------------------------ | --------------------------------- |
	| Only one wire - less expensive         | Not fault tolerant(No redundancy) |
	| Suited for temporary network         | Limited cable length              |
	| Node failures does not affect others | No security                       | 


- __Ring__
		- A ring topology is a bus topology in a closed loop.
		- Peer-to-Peer LAN topology
		- Two connections: one each of its nearest neighbors
		- Unidirectional 
		- Sending and receiving data takes place with the help of a ==token==
![[Ring Network.png | 300x300]]
| Advantages                             | Disadvantages                                                         |
| -------------------------------------- | --------------------------------------------------------------------- |
| Performance better than Bus topology   | Unidirectional. Single point of failure will affect the whole network |
| Can cause bottleneck due to weak links | Increase in load results in decrease in performance                   |
| All nodes with equal access            | No security                                                                                                  |                                                                       |
	
- Star
	- Every Node is connected to a central node called a hub or a switch
	- Centralized Management
	- All traffic must pass through the hub or switch
![[Extended Star Topology.png]]
| Advantages                             | Disadvantages                                       |
| -------------------------------------- | --------------------------------------------------- |
| Easy to design and implement           | Single point of failure affects the whole network   |
| Centralized administration | Bottlenecks due to overloaded switch/Hub |
| Scalable            | Increased cost due to switch/hub                                         |

- Mesh
	- Each node is directly connected to every other nodes in the network
	- Fault tolerant and reliable
![[Mesh Topology.png]]
| Advantages     | Disadvantages                            |
| -------------- | ---------------------------------------- |
| Fault Tolerant | Issues with broadcasting messages        |
| Reliable       | Expensiveand impractical for large networks |

- Hybrid
![[Hybrid Topology.png]]