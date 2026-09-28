# Programming Assignment 6: Written Report

## 1. Explanation of Graph Representation

My program represents a graph using an adjacency list.

* **Vertices:** The vertices represent the distinct entities or nodes in the graph. In my code, vertices are strings like "A", "B", and "C". They are stored as the keys in the `self.adj` dictionary.
* **Edges:** The edges represent the connections between the vertices. In my implementation, the `add_edge(u, v)` method creates an undirected edge, meaning the connection goes both ways between `u` and `v`.
* **Adjacency List Storage:** The adjacency list is a Python dictionary called `self.adj`. Each key is a vertex, and its value is a list of neighboring vertices. For example, if the graph has an edge between A and B, the dictionary stores `'A': ['B']` and `'B': ['A']`.
* **Why Adjacency Lists Are Useful:** Adjacency lists are space efficient, especially for sparse graphs that have relatively few edges. They only store the edges that actually exist, taking up O(V + E) space. An adjacency matrix would take O(V^2) space no matter how many edges exist. Also, finding a vertex's neighbors takes time proportional to the number of neighbors, which makes traversals like BFS very efficient.

## 2. Explanation of BFS

Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It explores the graph level by level, moving outward from the starting vertex.

* **How BFS chooses which vertex to visit next:** BFS uses a first in, first out approach. It visits all immediate neighbors of the starting vertex first, then all unvisited neighbors of those neighbors, and so on.
* **Why BFS uses a queue:** A queue enforces the level-by-level traversal. When a vertex is visited, its unvisited neighbors are added to the back of the queue. Because vertices are removed from the front of the queue using `popleft()` in my code, BFS finishes exploring the current level before moving on to the next level.
* **How BFS tracks visited vertices:** BFS uses a `visited` set to keep track of vertices that have already been discovered and added to the queue. Before adding a neighbor to the queue, the algorithm checks whether it is already in the `visited` set. This prevents infinite loops, especially in graphs with cycles, and ensures each vertex is processed exactly once.
* **What the traversal order tells us:** The traversal order shows which vertices are closest to the starting vertex. In an unweighted graph, vertices closer to the start (fewer edges away) appear earlier. The order also shows which vertices are unreachable, since they never appear in the output.

## 3. Test Results

Below is the output generated from running my test cases.

**Test 1: Connected graph**

* **Graph Structure:** Vertices: A, B, C, D, E. Edges: (A,B), (A,C), (B,D), (C,E).
* **Starting Vertex:** A. **BFS Traversal Order:** `['A', 'B', 'C', 'D', 'E']`
* **Starting Vertex:** E. **BFS Traversal Order:** `['E', 'C', 'A', 'B', 'D']`
* **Confirmation:** The program ran successfully and traversed all connected vertices.

**Test 2: Disconnected graph**

* **Graph Structure:** Vertices: A, B, C, D, E. Edges: (A,B), (B,C), (D,E). This graph has two disconnected components.
* **Starting Vertex:** A. **BFS Traversal Order:** `['A', 'B', 'C']`
* **Starting Vertex:** D. **BFS Traversal Order:** `['D', 'E']`
* **Confirmation:** The program ran successfully. The output confirms BFS only traverses the connected component containing the starting vertex.

**Test 3: Six-vertex graph with a cycle**

* **Graph Structure:** Vertices: A, B, C, D, E, F. Edges: (A,B), (A,C), (B,D), (C,D), (D,E), (E,F). The path A-B-D-C-A forms a cycle.
* **Starting Vertex:** A. **BFS Traversal Order:** `['A', 'B', 'C', 'D', 'E', 'F']`
* **Starting Vertex:** F. **BFS Traversal Order:** `['F', 'E', 'D', 'B', 'C', 'A']`
* **Confirmation:** The program ran successfully. The `visited` set prevented an infinite loop despite the cycle.

**Full program output:**

```
Test 1: connected graph
BFS from A:  ['A', 'B', 'C', 'D', 'E']
BFS from E:  ['E', 'C', 'A', 'B', 'D']
Test 2: disconnected from graph
BFS from A:  ['A', 'B', 'C']
BFS from D:  ['D', 'E']
Test 3: six vertex graph with a cycle
BFS from A: ['A', 'B', 'C', 'D', 'E', 'F']
BFS from F: ['F', 'E', 'D', 'B', 'C', 'A']
```

## 4. Runtime and Space Analysis

* **Meaning of V and E:** V is the number of vertices in the graph and E is the number of edges.
* **Runtime O(V + E):** BFS using an adjacency list runs in O(V + E). Each vertex is added to the queue once and removed once, which takes O(V) total. Each vertex's adjacency list is scanned once, when that vertex is removed from the queue. In an undirected graph, each edge appears in two adjacency lists, so each edge is looked at at most twice (once from each endpoint). That is still O(E). Adding the two parts gives O(V + E).
* **Queue Space Usage:** The queue can hold up to O(V) vertices in the worst case, such as a star graph where one vertex is connected to all the others.
* **Visited Set Space Usage:** The `visited` set stores each vertex at most once, so it also uses O(V) space.
* **Total Space:** The adjacency list itself takes O(V + E) space. The extra space BFS uses beyond the graph is O(V), from the queue and the visited set.
* **Graph Size and Performance:** The running time grows linearly with the size of the graph. As the number of vertices and edges grows, the work grows in proportion, and the memory for the queue and visited set grows with the number of vertices.

## 5. BFS vs. DFS Comparison

1. **How does BFS explore a graph?** BFS explores broadly, visiting all neighbors of a vertex at the current depth level before moving on to vertices at the next level.
2. **How does DFS explore a graph?** DFS explores deeply, following a single path as far as possible until it hits a dead end, then backtracking to try other paths.
3. **What data structure does BFS typically use?** A queue, which is first in, first out.
4. **What data structure or technique does DFS typically use?** A stack, which is last in, first out, or recursion, which uses the call stack.
5. **One situation where BFS may be more useful than DFS:** BFS is more useful for finding the shortest path between two vertices in an unweighted graph, since it finds the path with the fewest edges.

## 6. Reflection

This assignment helped me understand how graphs are structured and traversed in code. Before this, I understood the general idea of a graph from lecture, but actually building one from scratch made the details click. I learned that choosing the right representation, like an adjacency list, is crucial for memory efficiency, especially when dealing with sparse graphs where an adjacency matrix would waste space. It was interesting to see how a simple dictionary of lists could capture all the relationships in a graph so cleanly. Implementing BFS from scratch showed me the importance of the queue data structure in achieving a level by level traversal, and how a `visited` set is absolutely necessary to prevent infinite loops in graphs with cycles. I also learned that the order in which neighbors are added to the queue directly affects the traversal output, which I had not thought about before. Analyzing the algorithm helped me understand why BFS operates at O(V + E) time complexity, since every vertex and edge must be examined exactly once. Testing with a disconnected graph was also a good reminder that BFS only reaches vertices in the same component as the start. Overall, this assignment bridged the gap between theoretical graph concepts and practical algorithm implementation.

