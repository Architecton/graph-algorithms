import sys

# Node: class representing a node in an undirected graph.
class Node:
	def __init__(self, val, adjacent_nodes):
		self.val = val
		self.adjacent_nodes = adjacent_nodes

# Graph: class representing a simple undirected graph.
class Graph:
	def __init__(self, nodes):
		self.nodes = nodes

# is_float, is_int: auxiliary functions that check if value parsed from user can be connverted to float or int type.
def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def is_int(value):
  try:
    int(value)
    return True
  except ValueError:
    return False
#######################################

# construct graph: construct a graph by first parsing the number of nodes and edges
# and then parsing the values of nodes and then the edges. The nodes are indexed from
# 0 to N - 1, where N is the number of nodes. Indexing is done when the values in nodes are
# specified - the first created node is indexed with 0 and so on.
def construct_graph():
	while True:
		try:
			# Parse graph description from standard input.
			in_lines = sys.stdin.readlines()
			# Remove newline characters from input.
			in_lines = filter(lambda x: x != '', map(lambda x: x.replace('\n', ''), in_lines))

			# Parse number of nodes and edges.
			num_nodes = abs(int(next(in_lines)))
			num_edges = abs(int(next(in_lines)))

			# Define an empty list for storing nodes.
			nodes = []

			# Parse nodes.
			for i in range(num_nodes):
				# Parse next node value.
				val = next(in_lines)

				# Check if parsed input can be converted to float type.
				if is_float(val):
					val = float(val)

				# Check if parsed input can be converted to int type.
				if is_int(val):
					val = int(val)

				# Create Node instance with specified value.
				node = Node(val, [])

				# Add index to node.
				node.index = i

				# Initialize node as unvisited
				node.visited = False

				# Add node to list of nodes.
				nodes.append(node)

			# Parse edges.
			for i in range(num_edges):
				# Parse Nodes connected by edge.
				node_A = int(next(in_lines))
				node_B = int(next(in_lines))

				# Add pointers to adjacent node to nodes connected by the edge.
				nodes[node_A].adjacent_nodes.append(nodes[node_B])
				nodes[node_B].adjacent_nodes.append(nodes[node_A])

			# Return the constructed graph
			return Graph(nodes)

		except (ValueError("Illegal number of nodes"), IndexError("Index out of bounds"), StopIteration) as error:
			print("Invalid input. Please try again.")

# clear_visited: set attribute visited to False for all nodes in graph G.
def clear_visited(G):
	for node in G.nodes:
		node.visited = False