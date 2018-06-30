# -*- coding: utf-8 -*-
from graph import graph

def get_graph_from_file(filename):
	new_graph = graph()
	lines = []
	for line in open(filename):
		lines.append(line)

	number_of_nodes = int(lines[0])

	for i in range(number_of_nodes+1):
		new_graph.add_node(i)

	for i in range(1, len(lines)):

		# Pega o nó da direita e o nó da esquerda
		# e coloca ele em uma lista de 2 itens.
		# PS: strip retira o caracter '\n'.
		edge = lines[i].strip().split(' ')

		# add edge recebe um tupla que ele separa
		# internamente em dois nós separados.
		two_nodes = (int(edge[0]),int(edge[1]))

		# Se a aresta tiver peso
		if len(edge) > 2:
			weight = float(edge[2])
			new_graph.add_edge(edge=two_nodes, wt=weight, label=str(weight))

		else:
			new_graph.add_edge(edge=two_nodes)

	return new_graph

print("------grafo 2-------")
filename = "grafo2.graph"
grafo = get_graph_from_file(filename)
print(grafo.edges_and_weights())
print("------matrix adjacencia-------")
print(grafo.adjacency_matrix())
print("------lista adjacencia-------")
print(grafo.adjacency_list())
