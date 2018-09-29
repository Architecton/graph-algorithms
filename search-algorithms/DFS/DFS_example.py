import simple_graph

# Construct example graph from user input/file
G = simple_graph.construct_graph()

# recursive_DFS: A simple recursive depth-first search implementation
def recursive_DFS(v, to_find, trace):
	v.visited = True 							# Mark node as visited.
	if trace:									# Trace functionality
		print("visiting node " + str(v.index) + ".")
	if v.val == to_find: 										# If value in current node is the one we are looking for...
		return v  												# ...return it.
	for node in v.adjacent_nodes: 								# Go over adjacent nodes in graph.
		if node.visited == False: 								# Check if generated node has already been marked.
			res = recursive_DFS(node, to_find, trace = True) 	# Make recursive call for unmarked adjacent node.
			if res != None: 									# If found result return it.
				return res
	return None 												# If reached dead end, return None.

# recursive_DFS: A simple depth-first search implementation using a stack.
def iterative_DFS(v, to_find, trace):
	stack = [] 			# Create a simple stack represented by a list.
	v.visited = True 	# Mark starting node as visited.
	stack.append(v) 	# Push starting node onto stack.
	while(stack != []): 						# While stack is not empty...
		next_node = stack.pop() 				# ...pop next node from stack.
		if trace:
			print("visiting node " + str(next_node.index) + ".")
		if next_node.val == to_find: 			# If popped node is what we are looking for...
			return next_node 					# ...return found node.
		for node in next_node.adjacent_nodes: 	# Else push unvisited adjacent nodes onto stack.
			if node.visited == False:
				node.visited = True
				stack.append(node)
				if trace: 						# Trace functionality
					print("pushing node " + str(node.index) + " to stack.")
	return None 								# If stack emptied without finding sought after value, return None.

# Use examples ########################################################

# Searching for values found in the graph #####

# we are looking for node with value 'd'.
to_find = 'a'

print("Looking for node with value ´" + str(to_find) + "´...")

# Find using recursive DFS search.
res = recursive_DFS(G.nodes[0], to_find, trace = True)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.\n")
else:
	print("Node with value ´" + str(to_find) + "´ not found.\n")

# Mark all nodes as unvisited.
simple_graph.clear_visited(G)

# we are looking for node with value 'd'.
to_find = 'd'

print("Looking for node with value ´" + str(to_find) + "´...")

# Find using recursive DFS search.
res = iterative_DFS(G.nodes[0], to_find, trace = True)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.\n")
else:
	print("Node with value ´" + str(to_find) + "´ not found.\n")

# Mark all nodes as unvisited.
simple_graph.clear_visited(G)

# Searching for values not found in the graph #####

# we are looking for node with value 'f'.
to_find = 'f'

print("Looking for node with value ´" + str(to_find) + "´...")

# Find using recursive DFS search.
res = recursive_DFS(G.nodes[0], to_find, trace = True)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.\n")
else:
	print("Node with value ´" + str(to_find) + "´ not found.\n")

# Mark all nodes as unvisited.
simple_graph.clear_visited(G)

# we are looking for node with value 'z'.
to_find = 'z'

print("Looking for node with value ´" + str(to_find) + "´...")

# Find using recursive DFS search.
res = iterative_DFS(G.nodes[0], to_find, trace = True)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.\n")
else:
	print("Node with value ´" + str(to_find) + "´ not found.\n")

# Mark all nodes as unvisited.
simple_graph.clear_visited(G)
########################################################################