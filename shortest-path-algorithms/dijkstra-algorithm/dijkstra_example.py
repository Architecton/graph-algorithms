import simple_graph2

# dijkstra: implementation of Dijkstra's algorithm with trace printing functionality
def dijkstra(G, source, trace):
	
	#neighbors: auxiliary function that returns the neighbors of Node node and te edge connecting them as a dict
	def neighbors(node):
		neighbors = [] 				# Define empty list for storing the results.
		for edge in G.edges: 		# Go over edges in graph.
			if edge.node_1.index == node.index: 	# If found edge that connects to neighbor, add to list of results.
				neighbors.append({'node' : edge.node_2, 'edge' : edge})
			if edge.node_2.index == node.index:
				neighbors.append({'node' : edge.node_1, 'edge' : edge})
		
		if trace:
			print("Neighbors of node with index {0} are:".format(node.index))
			for n in neighbors:
				print(n["node"].index)

		# Return list of neighbors and edges.
		return neighbors

	# Create a list of unvisited nodes and initialize distance and prev properties.
	unvisited = G.nodes.copy()
	for node in unvisited:
		node.distance = float('inf')
		node.prev = None
	source.distance = 0
	
	# Sort list of unvisited nodes by distance
	unvisited.sort(key = lambda x : x.distance, reverse = True)

	# While list of unvisited nodes is not empty...
	while len(unvisited) > 0:
		u = unvisited.pop()
		if trace:
			print('Visiting node with index ' + str(u.index))
		for node_edge in neighbors(u): 			# Go over neighbor nodes and compute if it is cheaper to get to neighbor via this node.
			if trace:
				print('Inspecting neighbor node with index ' + str(node_edge["node"].index))
			alt = u.distance + node_edge["edge"].weight 	# Compute alternative distance to neighbor via this node.
			if trace:
				print("\nalt weight is {0}".format(alt))
			if alt < node_edge["node"].distance: 			# If this route is cheaper, assign new distance to neighbor and update prev.
				node_edge["node"].distance = alt
				node_edge["node"].prev = u
	return G.nodes

## Simple Test #####################################################################################

G = simple_graph2.construct_graph()

V = dijkstra(G, G.nodes[0], trace = True)

print("Minimum distances from source node {0} to other nodes are:".format(G.nodes[0].index))
for node in V:
	print("To node {0}: {1}".format(node.index, node.distance))

#####################################################################################################