#### Q 1: Identify the given topology and determine how many cables and ports are required to have such a network?

![[Ring Topology.png]]

| No of Nodes (N) | No of Cables(=N) | No of Ports/Device (NOP) | Total No of ports in the network (TNOP) = N X NOP |
| --------------- | ---------------- | ------------------------ | ------------------------------------------------- |
| 2               | 2                | 2                        | 4                                                 |
| 3               | 3                | 2                        | 6                                                 |
| 4               | 4                | 2                        | 8                                                 |
| N               | N                | 2                        | 2 x N                                                  |

----------------------------------------------------------------------
#### Q 2 : Traffic problem can be minimized using?
a. Star
b. Bus
c. Ring
d. ==Mesh==

-----------------------------------------------------------------------

#### Q 3: How many ports and cables links are needed for a start topology?

![[Star Topology.png]]

| No of Nodes (N) | No of Cables(=N) | No of Ports/Device (NOP) | Total No of ports in the network (TNOP) = N X NOP |
| --------------- | ---------------- | ------------------------ | ------------------------------------------------- |
| 2               | 2                | 1                        | 4                                                 |
| 3               | 3                | 1                        | 6                                                 |
| 4               | 4                | 1                        | 8                                                 |
| N               | N                | 1                        | 2 x N                                             |

----------------------------------------------------------------------

#### Q 4: Assume six devices are arranged in a mesh topology.
#### 1. How many cables are needed?
#### 2. How many ports are needed for each device?
#### 3. How many ports are there in the netire network?


| No of Nodes (N) | No of Cables (=N*(N-1)/2) | No of Ports/Device (NOP) = (N-1)| Total No of ports in the network (TNOP) = N X NOP |
| --------------- | ------------------ | ------------------------------- | ------------------------------------------------- |
| 2               | 1                  | 1                               | 2                                                 |
| 3               | 3                  | 2                               | 6                                                 |
| 4               | 6                  | 3                               | 12                                                |
| 5               | 9                  | 4                               | 20                                             |
|                 |                    |                                 |                                                   |
