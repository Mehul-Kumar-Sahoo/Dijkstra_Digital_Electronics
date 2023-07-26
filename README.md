# DIJKSTRA ALGORITHM USING DIGITAL ELECTRONICS

Skills: Proteus 7, Digital Electronics, Algorithm

 - I am Mehul Kumar Sahoo, and I am pursuing Electronics Engineering at IIT(BHU), Varanasi. This repository contains a 
simulation for the digital circuit for the Dijkstra algorithm (maximum eight nodes).

 - The "Dijkstra_Final.dsn" file contains the design file that runs on **Proteus Software**.

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


