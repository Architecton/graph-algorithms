import simple_graph

# Construct example graph.
G = simple_graph.construct_graph()

# IDS: simple iterative deepening search implementation
def IDS(v, to_find, trace):
	# limited_DFS: simple DFS implementation with depth limit
	def limited_DFS(v, depth):
		if trace:
			print("Visiting node " + str(v.index) + " with value " + str(v.val) +  "...")
		v.visited = True
		if v.val == to_find: 	# If visited node contains the sought value, return it.
			return v
		if depth <= 0: 			# If exceeded maximum search depth, treat as dead end.
			return None
		for node in v.adjacent_nodes: 				# Go over adjacent nodes and make recursive call with decremented depth.
			if node.visited == False:
				node.visited = True
				res = limited_DFS(node, depth - 1)
				if res != None: 					# If found result, return it.
					return res
		return None

	# Go over specified depths.
	for i in range(1, 10):
		if trace:
			print("Searching with maximum depth equal to " + str(i) + ".")
		res = limited_DFS(v, i)
		simple_graph.clear_visited(G) 	# Clear visited markers.
		if res != None: 				# If found node with sought value, return it.
			return res
	return None

# Define a value we are looking for.
to_find = 'e'

# Try to find value to_find using iterative deepening search implemented with the IDS function.
res = IDS(G.nodes[0], to_find, trace = True)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.")
else:
	print("Node with value ´" + str(to_find) + "´ not found.")