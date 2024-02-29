def string_reconstruction(k, patterns):
    # Create an adjacency list for the de Bruijn graph
    graph = {}
    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]

    # Find the Eulerian path in the de Bruijn graph
    path = eulerian_path(graph)

    # Reconstruct the string from the Eulerian path
    text = path[0]
    for i in range(1, len(path)):
        text += path[i][-1]

    return text

def eulerian_path(graph):
    # Find the Eulerian path using Fleury's algorithm
    current_node = list(graph.keys())[0]
    circuit = []
    stack = [current_node]

    while stack:
        if current_node in graph and graph[current_node]:
            stack.append(current_node)
            next_node = graph[current_node].pop()
            current_node = next_node
        else:
            circuit.append(current_node)
            current_node = stack.pop()

    # Reverse the circuit to get the Eulerian path
    return circuit[::-1]

# Example usage
k = 3
pattern = "AAT  ATG  ATG  ATG  CAT  CCA  GAT  GCC  GGA  GGG  GTT  TAA  TGC  TGG  TGT" 

patterns = pattern.split()

result = string_reconstruction(k, patterns)
print(result)
