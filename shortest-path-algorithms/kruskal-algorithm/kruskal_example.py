import simple_graph2

# same_set: check if Nodes node_1 and node_2 belong to the same set of nodes.
def same_set(node_1, node_2, d_set):
	for s in d_set:						# Go over sets.
		if node_1 in s and node_2 in s: # If both nodes found in same set, return True.
			return True
	return False 						# If both nodes not sound in any set, return False.

# set_union: apply union operation to sets containing Nodes node_1 and node_2.
# Return disjunct set with sets containing node_1 and node_2 replaced with their union.
def set_union(node_1, node_2, d_set):
	# Define set pointers.
	s1 = None
	s2 = None
	# Find sets containing node_1 and node_2.
	for i in range(len(d_set)):
		if node_1 in d_set[i]:
			s1 = d_set[i]
		if node_2 in d_set[i]:	
			s2 = d_set[i]
		if s1 != None and s2 != None:
			break

	# Make a copy of the original list representing the set.
	res_set = d_set.copy()

	# Remove sets pointed to by s1 and s2 and append union of s1 and s2.
	res_set.remove(s1)
	res_set.remove(s1)
	res_set.append(s1 | s2)

	# Return result.
	return res_set


# kruskal: implementation of Kruskal's algorithm. Returns set containing edges representing the
# resulting minimum spanning tree.
def kruskal(G):
	MST = set() 		# Define set for storing edges forming the resulting minimum spanning tree.
	nodes = [] 			# Define list for storing sets of nodes representing trees.
	for node in G.nodes: 									# Put every node in its own set (every node is a tree).
		nodes.append({node})
	edges = G.edges.copy().sort(key = lambda x : x.weight) 	# Make a list of edges sorted by their weights.

	for edge in edges: 											# Go over edges in list of edges in graph sorted by edge weight.
		if not same_set(edge.node_1, edge.node_2, nodes): 		# If nodes connected by the edges are in different trees (different sets)...
			MST.add(edge) 										# ...add edge to minimum spanning tree.
			nodes = set_union(edge.node_1, edge.node_2, nodes) 	# The trees connected by the edge are now connected. Create union of vertices.
	return MST 													# Return set of edges representing the minimum spanning tree