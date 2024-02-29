def de_bruijn_graph(patterns):
    graph = {}
    
    # Create nodes and edges from k-mers
    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        
        if prefix not in graph:
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    
    # Sort the adjacency lists
    for node in graph:
        graph[node].sort()
    
    return graph

# Sample Input
pattern = "GAGG CAGG GGGG GGGA CAGG AGGG GGAG"
patterns = pattern.split()
# Constructing the de Bruijn graph
result_graph = de_bruijn_graph(patterns)

# Print the result in the specified format
for node in result_graph:
    neighbors = result_graph[node]
    if neighbors:
        print(f"{node}: {' '.join(neighbors)}")

#run this code in python playground because here it gives incomplete op. try to incorporate 1) 2) in this and find the count of the edges generated.
