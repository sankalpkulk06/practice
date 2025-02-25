import numpy as np

def pagerank(graph, d=0.85, max_iter=100):
    nodes = list(graph.keys())
    N = len(nodes)
    M = np.zeros((N, N))
    
    # map each node to its index
    node_index = {}  
    index = 0  

    for node in nodes:
        node_index[node] = index  
        index += 1

    for node in graph:
        if graph[node]:
            for out_node in graph[node]:
                M[node_index[out_node], node_index[node]] = 1 / len(graph[node])
    
    ranks = np.ones(N) / N  # Initialize ranks 
    E = np.ones(N) / N  # 1 / N
    
    for iteration in range(max_iter):
        # r = (1-d).E + d.M.r (from lecture notes)
        new_ranks = d * np.dot(M, ranks) + (1 - d) * E
        
        # stops when the difference between iterations is below 0.01
        if np.linalg.norm(new_ranks - ranks, 1) < 0.01:
            print(f"Converged in {iteration + 1} iterations")
            break
        
        ranks = new_ranks
        print(f"Iteration {iteration+1}: {dict(zip(nodes, ranks))}")
    

# Define the graph 
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'E'],
    'C': [],
    'D': ['A'],
    'E': ['A', 'C']
}

# Case 1: Compute pagerank
print("PageRank for full graph:")
pagerank(graph)

# Case 2: Only 'A' in the base set (i.e., only A has outgoing links)
base_graph = {'A': ['B'], 'B': [], 'C': [], 'D': [], 'E': []}
print("\nPageRank with only A in base set:")
pagerank(base_graph)
