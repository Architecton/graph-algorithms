import numpy as np

# Create an example graph represented as an edge weights matrix.
G = np.array([[0, 2, 3, 4], [1, 0, 5, 6], [7, 7, 0, 8], [1, 2, 3, 0]])

# floyd_warshall: function implementing the Floyd-Warshall algorithm. The function returns the matrix representation of
# minimum paths from every vertex to every other vertex.
def floyd_warshall(G):
	G_temp = G.copy()
	for k in range(len(G_temp)): 					# Go over all "via" nodes.
		for i in range(len(G_temp)): 				# Check if it is cheaper to get from node i to node j via node k and if so,
			for j in range(len(G_temp)): 			# update distance.
				if G_temp[i][j] > G_temp[i][k] + G_temp[k][j]:
					G_temp[i][j] = G_temp[i][k] + G_temp[k][j]
	return G_temp

# Call function floyd_warshall on example graph G.
print("Matrix representing the graph before calling the Floyd-Warshall implementing function:")
print(G)

print("\nMatrix representing the graph after calling the Floyd-Warshall implementing function:")
R = floyd_warshall(G)
print(R)