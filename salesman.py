from itertools import permutations

def tsp_brute_force(graph):
    nodes=list(graph.keys())
    shortest_path=None
    min_cost=float('inf')

    for perm in permutations(nodes):
        cost=sum(graph[perm[i]][perm[i+1]]for i in range (len(perm)-1))
        cost+=graph[perm[-1]][perm[0]]

        if cost < min_cost:
            min_cost=cost
            shortest_path=perm

    return shortest_path,min_cost

def input_graph():
    graph={}
    n=int(input("Enter the number of nodes : "))
    print("enter the nodes(separated by space) :")
    nodes=input().split()

    for node in nodes:
        graph[node]={}
    print ("Enter the distance between nodes :")

    for i in range(n):
        for j in range (i+1 , n):
            print(f"Distance between nodes {nodes[i]} and {nodes[j]}:",end="")
            distance=int(input())
            graph[nodes[i]][nodes[j]] = distance
            graph[nodes[j]][nodes[i]] = distance
    return graph
    
# Main program
graph = input_graph()  # Get the graph input from the user
path, cost = tsp_brute_force(graph)  # Solve the TSP problem using the brute-force method
print("Shortest Path:", path, "with Cost:", cost)  # Print the shortest path and its cost

    