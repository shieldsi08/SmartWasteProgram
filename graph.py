from random import randint
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.neighbours = []
    def addNeighbour(self):
        neighbour = Node(randint(1,10))
        self.neighbours.append(neighbour)
        neighbour.neighbours.append(self)
        return neighbour
    def removeNeihbour(self,node):
        self.neighbours.pop(node)

class Edge:
    def __init__(self,value) -> None:
        self.value
