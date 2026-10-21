from graph import *
from random import randint
def generateCity(num):
    nodes = []

    for node in range(num):
        nodes.append(Node(randint(1,10)))
    print(nodes)

generateCity(10)