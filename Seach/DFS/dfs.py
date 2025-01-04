"""
- DFS from a Given Source of Undirected Graph
"""

def dfs_rec(adj, visited, s):
    visited[s] = True
    print(s, end=" ")

    # Recursively visit all the adjacent vertices that are not visited
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, s):

    visited = [False] * len(adj)

    dfs_rec(adj, visited, s)


def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)
    
if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)