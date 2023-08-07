# DIJKSTRA ALGORITHM USING DIGITAL ELECTRONICS

Skills: Proteus 7, Digital Electronics, Algorithm

 - I am Mehul Kumar Sahoo, and I am pursuing Electronics Engineering at IIT(BHU), Varanasi. This repository contains a 
simulation for the digital circuit for the Dijkstra algorithm (maximum eight nodes).

 - The "Dijkstra_Final.dsn" file contains the design file that runs on **Proteus Software**.
 - The complete circuit is as follows.
   
<img width="793" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/15c90764-4035-400b-892f-faa976e2e366">

 - The graph is stored in 8 different Binary files (.bin format) where each file contains one row of modified
adjacency matrix.

**Dijkstra Algorithm** – It is a greedy algorithm that helps us to find the shortest paths from the source to all
vertices in a given graph.

Let us take an example of a graph to make it easy for us to understand.
    <img width="626" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/c61df0e3-3268-418f-bca5-21d53afff048">

 - (Here, consider A, B, C, D, and E as 0,1,2,3,4 for convenience)
 - For the given graph, the ideal adjacency matrix (8x8) should be
   
    <img width="461" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/af5ce370-89b6-43fe-a08e-a13687d4c050">


 - Here we will use a modified adjacency matrix.
 - To modify the adjacency matrix, we will replace the ones with the distance between two consecutive nodes and will
replace the zeros with infinite distance, which in this particular digital circuit is 15. So the modified adjacency matrix will be:-
   
    <img width="457" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/2f6a1dad-2c22-4ef9-ae64-df8d18f34dec">

 -  After the adjacency matrix is modified, we will take each row and make its binary file, which is given as input
to the ROM. (The Python code for making binary files and the binary files are provided in the repository)

## CIRCUIT EXPLANATION
 - **Input** - We have used ROM (IC2732) and counters(IC74161) for input.
 - **Source Node** - The circuit finds the node along with the minimum distance from it and assigns it as the next node,
and the gateway takes the distance value to the required node.

   <img width="626" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/f3404d9d-e4db-4c8a-8ea7-38dbe4fe2a60">

 - The remaining circuit mainly consists of two parts: - Controller and Gateway.
   - The function of the **controller** is to calculate, i.e., find the minimum distance of the current node from the
source node and find the next node at the minimum distance from it.
   - The **gateway's** function is to receive the next node and its minimum distance from the source node and take the values to the next node.

 - **Controller** - The basic layout of the controller is as follows:-

   <img width="515" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/62a001f4-6c62-46ae-8d56-bc453d8023ea">

 -	First, it receives the minimum distance from the previous node, and when it gets the enable bit, it starts behaving as the current node.
 - Then, the counters start counting from 0 to 7, which is fed into the ROM to extract the data.
 - The next part finds the minimum distance of the next node from the current node and ensures that it is not visited earlier.
 - The bottom part of the circuit finds the minimum distance of the current node from the source node through all possible paths received.
   
 - **Gateway** :- It consists of three parts
    - XNOR gates for bit matching to channel the distance value to the next node by providing the select line for the 6x3 multiplexers.
      
      <img width="587" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/087b64ef-e506-478b-99db-dee5f50cb4b9">

    - 6x3 Multiplexers are present whose output is the distance whenever it is in state one else output is 0.
      
      <img width="605" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/15c78f48-789a-4031-a7d6-f09cd1c669a2">

    -  3x8 decoder provides the enable bit for the processor of the next node.
     
        <img width="230" alt="image" src="https://github.com/Mehul-Kumar-Sahoo/Dijkstra_Digital_Electronics/assets/93527557/2c92fd66-ccde-414f-a6d5-d30559816a66">

## OUTPUT
- The output is shown using logic probes and only checks the nodes for which the graph is made (for other unused nodes, it gives garbage value).
