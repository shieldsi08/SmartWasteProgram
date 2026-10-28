from graph import *
from random import randint

import matplotlib.pyplot as plt
import networkx as nx


g = Graph()


amountofnodes = randint(20, 40)
blocksize = randint(10,20)
blocks = []
created_nodes = []
for i in range(blocksize):
    block = []
    for j in range(blocksize):
        block.append([])
    blocks.append(block)



for i in range(amountofnodes):
    flag = False
    while not flag:
        x = randint(0, blocksize - 1)
        y = randint(0, blocksize - 1)
        if blocks[x][y] == []:
            flag = True
    new_node = Node(i, x, y)
    blocks[x][y].append(new_node)
    g.addNode(new_node)


    if created_nodes:
        number_of_edges = randint(1, min(3, len(created_nodes)))
        for _ in range(number_of_edges):
            neighbour = created_nodes[randint(0, len(created_nodes) - 1)]
        g.addEdge(new_node, neighbour)
    created_nodes.append(new_node)




g.display()
g.visualize()