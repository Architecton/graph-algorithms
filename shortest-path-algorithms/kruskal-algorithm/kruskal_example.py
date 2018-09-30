import simple_graph2

def kruskal(G):
	MST = []
	nodes = []
	for node in G.nodes:
		nodes.append({node})
	edges = sort(G.edges)
	for edge in edges:
		if not same_set(edge.node_1, edge.node_2):
			MST.append(edge)
			set_union(edge.node_1, edge.node_2, nodes)
	return 