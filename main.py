from graph import *
from random import randint
def generateCity(num):
    nodes = []
    nodes = addnodes(nodes,num)
    nodes = addNeighbours(nodes)
    
    
    print(nodes)
def addnodes(nodes,num):
    for node in range(num):
        nodes.append(Node(randint(1,10)))
    return nodes
def addNeighbours(nodes):
    for node in nodes:
        for i in range(randint(0,10)):
            neighbour = node.addNeighbour()
            nodes.append(neighbour)
    return nodes
generateCity(10)