from graph import *
from random import randint

import matplotlib.pyplot as plt
import networkx as nx
# def generateCity(num):
#     nodes = []
#     nodes = addnodes(nodes,num)
#     nodes = addNeighbours(nodes)
    
    
#     print(nodes)
# def addnodes(nodes,num):
#     for node in range(num):
#         nodes.append(Node(randint(1,10)))
#     return nodes
# def addNeighbours(nodes):
#     for node in nodes:
#         for i in range(randint(0,10)):
#             neighbour = node.addNeighbour()
#             nodes.append(neighbour)
#     return nodes
# generateCity(10)

g = Graph()

# node1 = Node(1)
# node2 = Node(2)
# g.addNode(node1)
# g.addNode(node2)
# g.addEdge(node1, node2)
amountofnodes = randint(20, 40)
blocksize = randint(10,20)
blocks = []
created_nodes = []
for i in range(blocksize):
    block = []
    for j in range(blocksize):
        block.append([])
    blocks.append(block)
#2D array of blocks, each block is a list of nodes



for i in range(amountofnodes):
    flag = False
    while not flag:
        x = randint(0, blocksize - 1)
        y = randint(0, blocksize - 1)
        if blocks[x][y] == []:
            flag = True
    new_node = Node(i, x, y)  # Assign random x, y coordinates
    blocks[x][y].append(new_node)
    g.addNode(new_node)

    # Connect to earlier nodes so the new node always has eligible neighbours.
    if created_nodes:
        number_of_edges = randint(1, min(3, len(created_nodes)))
        for _ in range(number_of_edges):
            neighbour = created_nodes[randint(0, len(created_nodes) - 1)]
        g.addEdge(new_node, neighbour)
    created_nodes.append(new_node)



    # Randomly connect the new node to existing nodes
    # existing_nodes = list(g.adjacencyList.keys())
    # if existing_nodes:
    #     num_edges = randint(1, min(3, len(existing_nodes)))  # Limit the number of edges to avoid too many connections
    #     for _ in range(num_edges):
    #         neighbour = existing_nodes[randint(0, len(existing_nodes) - 1)]
    #         if new_node.value != neighbour.value:  # Avoid self-loop
    #             g.addEdge(new_node, neighbour)

g.display()
g.visualize()