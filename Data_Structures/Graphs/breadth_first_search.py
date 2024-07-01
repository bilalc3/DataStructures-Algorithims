from collections import deque

# Function to perform Breadth First Search on a graph
def bfs(adjList, startNode, visited):
    
    
    q = deque()
    
    while q:
        # take off next node 
        n = q.popleft()
        print(n)
        
        for v in adjList[n]:
            if v not in visited:
                q.append(v)
    
# Function to add an edge to the graph
def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    # Number of vertices in the graph
    vertices = 5

    # Adjacency list representation of the graph
    adjList = [[] for _ in range(vertices)]

    # Add edges to the graph
    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 2, 4)

    # Mark all the vertices as not visited
    visited = [False] * vertices

    # Perform BFS traversal starting from vertex 0
    print("Breadth First Traversal starting from vertex 0:", end=" ")
    bfs(adjList, 0, visited)

if __name__ == "__main__":
    main()