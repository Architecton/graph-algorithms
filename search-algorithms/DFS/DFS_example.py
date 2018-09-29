import simple_graph

# Construct example graph from user input/file
G = simple_graph.construct_graph()

# recursive_DFS: A simple recursive depth-first search implementation
def recursive_DFS(v, to_find):
	v.visited = True 							# Mark node as visited.
	if v.val == to_find: 						# If value in current node is the one we are looking for...
		return v  								# ...return it.
	for node in v.adjacent_nodes: 				# Go over adjacent nodes in graph.
		if not hasattr(node, 'visited'): 		# Check if generated node has already been marked.
			res = recursive_DFS(node, to_find) 	# Make recursive call for unmarked adjacent node.
			if res != None: 					# If found result return it.
				return res
	return None 								# If reached dead end, return None.

# recursive_DFS: A simple depth-first search implementation using a stack.
def iterative_DFS(v, to_find):
	stack = [] 			# Create a simple stack represented by a list.
	v.visited = True 	# Mark starting node as visited.
	stack.append(v) 	# Push starting node onto stack.

	while(stack != []): 						# While stack is not empty...
		next_node = stack.pop() 				# ...pop next node from stack.
		if next_node.val == to_find: 			# If popped node is what we are looking for...
			return next_node 					# ...return found node.
		for node in next_node.adjacent_nodes: 	# Else push unvisited adjacent nodes onto stack.
			if not hasattr(node, 'visited'):
				node.visited = True
				stack.append(node)
	return None 								# If stack emptied without finding sought after value, return None.

# Use examples ########################################################

# Searching for values found in the graph #####

# we are looking for node with value 'd'.
to_find = 'a'
# Find using recursive DFS search.
res = recursive_DFS(G.nodes[0], to_find)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.")
else:
	print("Node with value ´" + str(to_find) + "´ not found.")

# we are looking for node with value 'd'.
to_find = 'd'
# Find using recursive DFS search.
res = iterative_DFS(G.nodes[0], to_find)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.")
else:
	print("Node with value ´" + str(to_find) + "´ not found.")

# Searching for values not found in the graph #####

# we are looking for node with value 'f'.
to_find = 'f'
# Find using recursive DFS search.
res = recursive_DFS(G.nodes[0], to_find)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.")
else:
	print("Node with value ´" + str(to_find) + "´ not found.")

# we are looking for node with value 'z'.
to_find = 'z'
# Find using recursive DFS search.
res = iterative_DFS(G.nodes[0], to_find)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.")
else:
	print("Node with value ´" + str(to_find) + "´ not found.")

########################################################################