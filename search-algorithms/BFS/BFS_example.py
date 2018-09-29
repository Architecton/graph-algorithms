import simple_graph

# BFS: a simple implementation of the breadth-first graph search algorithm
def BFS(v, to_find, trace):
	queue = [] 					# Define an empty queue implemented using a list.
	v.visited = True 			# Mark starting node as visited.
	queue.append(v) 			# Add starting node to queue.
	while(queue != []): 			# While queue is not empty..
		next_node = queue.pop(0) 	# Get node from queue and visit it.
		if trace:
			print("Visiting node " + str(next_node.index) + ".")
		if next_node.val == to_find:
			return next_node
		for node in next_node.adjacent_nodes: 	# Go over nodes adjacent to next_node (node taken from queue).
			if node.visited == False: 			# If adjacent node is unvisited, mark as visited and add to queue.
				node.visited = True
				if trace:
					print("Adding node " + str(node.index) + " to queue.")
				queue.append(node)
	return None 								# If emptied queue before finding sought after node, return None.

# Construct graph from graph description passed through stdin input.
G = simple_graph.construct_graph()

# We are looking for node with value 'e'.
to_find = 'e'

# Try to find node with value 'e' using breadth-first search implemented with BFS method.
res = BFS(G.nodes[0], to_find, trace = True)
if res != None:
	print("Found node with value ´" + str(to_find) + "´.")
else:
	print("Node with value ´" + str(to_find) + "´ not found.")

