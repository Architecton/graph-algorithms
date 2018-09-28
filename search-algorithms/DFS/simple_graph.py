# Node: class representing a node in an undirected graph.
class Node:
	def __init__(self, val, adjacent_nodes):
		self.val = val
		self.adjacent_nodes = adjacent_nodes

# Graph: class representing a simple undirected graph.
class Graph:
	def __init__(self, nodes):
		self.nodes = nodes

# construct graph: construct a graph by first parsing the number of nodes and edges
# and then parsing the values of nodes and then the edges. The nodes are indexed from
# 0 to N - 1, where N is the number of nodes. Indexing is done when the values in nodes are
# specified - the first created node is indexed with 0 and so on.
def construct_graph():
	while True:
		try:
			# Parse number of nodes and edges.
			num_nodes = abs(int(input()))
			num_edges = abs(int(input()))

			# Define an empty list for storing nodes.
			nodes = []

			# Parse nodes.
			for i in range(num_nodes):
				# Parse next node value.
				val = input()
				# Add node to list of nodes.
				nodes.append(Node(val, []))

			# Parse edges.
			for i in range(num_edges):
				# Parse Nodes connected by edge.
				node_A = int(input())
				node_B = int(input())

				# Add pointers to adjacent node to nodes connected by the edge.
				nodes[node_A].adjacent_nodes.append(nodes[node_B])
				nodes[node_B].adjacent_nodes.append(nodes[node_A])

			# Return the constructed graph
			return Graph(nodes)

		except (ValueError("Illegal number of nodes"), IndexError("Index out of bounds")) as error:
			print("Invalid input. Please try again.")