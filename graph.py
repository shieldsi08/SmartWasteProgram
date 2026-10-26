from random import randint
import matplotlib.pyplot as plt
import networkx as nx
class Graph:
    def __init__(self) -> None:
        # Maps a Node object to a list of its neighbour Node objects
        self.adjacencyList = {}

    def addNode(self, node):
        if node not in self.adjacencyList:
            # FIX: Initialize with an empty list to store its neighbours
            self.adjacencyList[node] = []

    def addEdge(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        # FIX: Append to the list value, not the dictionary itself
        if node2 not in self.adjacencyList[node1]:
            self.adjacencyList[node1].append(node2)
        if node1 not in self.adjacencyList[node2]:
            self.adjacencyList[node2].append(node1)
        print(f"Added edge between {node1.value} and {node2.value}")
    def removeEdge(self, node1, node2):
        if node1 in self.adjacencyList and node2 in self.adjacencyList[node1]:
            self.adjacencyList[node1].remove(node2)
        if node2 in self.adjacencyList and node1 in self.adjacencyList[node2]:
            self.adjacencyList[node2].remove(node1)

    def removeNode(self, node):
        if node in self.adjacencyList:
            # Remove this node from all its neighbours' lists
            for neighbour in self.adjacencyList[node]:
                self.adjacencyList[neighbour].remove(node)
            # Delete the node from the graph
            del self.adjacencyList[node]

    def display(self):
        for node in self.adjacencyList:
            print(f"{node.value}: {[neighbour.value for neighbour in self.adjacencyList[node]]}")

    def visualize(self):
        """Draws the graph with rigid grid positioning like a city layout."""
        G = nx.Graph()
        
        # We will build a dictionary of coordinates for NetworkX to use
        # Format: { node_value: (x_coordinate, y_coordinate) }
        pos = {}
        
        for node, neighbours in self.adjacencyList.items():
            G.add_node(node.value)
            
            # FIX: Grab the x, y coordinates we saved inside our Node objects
            pos[node.value] = (node.x, node.y)
            
            for neighbour in neighbours:
                G.add_edge(node.value, neighbour.value)
        
        # Draw the graph using our strict city grid coordinates
        nx.draw(
            G, 
            pos=pos,              # Tells NetworkX EXACTLY where to put each circle
            with_labels=True, 
            node_color='#2ec4b6',   # Nice city-blueprint teal
            node_size=900, 
            font_size=11, 
            font_color='white',
            font_weight='bold', 
            edge_color='#cbd5e1',   # Clean street lines
            width=3
        )
        
        # Turn on the grid lines in the background so it looks like a blueprint map
        plt.grid(True, which='both', color='#f1f5f9', linestyle='-', linewidth=1)
        plt.gca().set_axisbelow(True) # Puts grid lines behind the nodes
        
        plt.title("City Grid Layout (No Clipping)", fontsize=14, fontweight='bold')
        plt.show()

class Node:
    def __init__(self, value,x,y) -> None:
        self.value = value
        self.x = x
        self.y = y
    # Python needs this to use the Node object as a dictionary key safely
    def __repr__(self):
        return f"Node({self.value})"