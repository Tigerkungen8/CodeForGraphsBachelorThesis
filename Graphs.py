import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure


############# TEST
import tkinter as tk
##################


global fig
fig = Figure(figsize=(5, 4), dpi=100)

class Graph():
    def __init__(self, edgeList = None, nodeList=None, treewidth=None, treeDecomposition=None):
        self.edgeList = [] if edgeList is None else edgeList
        self.nodeList = [] if nodeList is None else nodeList
        self.treewidth = treewidth
        self.treeDecomposition = treeDecomposition
        self.G = nx.Graph()


    def __str__(self):
        return f'Graph \n Edgelist: {self.edgeList} \n Nodelist: {self.nodeList} \n Treewidth: {self.treewidth}'

    def initiateGraph(self):
        if len(self.edgeList)==0 and len(self.nodeList)==0:
            return self.G
        else:
            self.G.add_nodes_from(self.nodeList)
            self.G.add_edges_from(self.edgeList)
            return self.G
        
    def addNode(self, nodes):
        self.G.add_nodes_from(nodes)

    def addEdge(self, edges):
        self.G.add_edges_from(edges)

    def removeNode(self, removeNodes):
        self.G.remove_nodes_from(removeNodes)

    def removeEdge(self, removeEdges):
        self.G.remove_edges_from(removeEdges)

    """ 
    def listToMatrix(self, lst):

        pass
    
    def matrixToList(self, mat):
        pass 
    """

    def newLists(self, newNodeList=None, newEdgelist=None):
        print("SELF: ",self)
        print(self.edgeList)
        self.edgeList = newEdgelist #if newEdgelist != None else self.edgeList
        self.nodeList = newNodeList #if newNodeList != None else self.nodeList
        return "Updated lists"

    def updateGraph(self):
        self.G.add_nodes_from(self.nodeList)
        self.G.add_edges_from(self.edgeList)
        return self.G

    def getTreewidth(self):
        k, TD = nx.algorithms.approximation.treewidth(self.G) # k = treewidth, TD = heuristic Tree Decomposition (not necessarily minimal)
        self.treewidth = k
        self.treeDecomposition = TD
        return k

    def createHopefullyMinimalTreeDecomposition(self, treewidth):
        pass


    def generatePLTFromGraph(self):
        #global fig
        #fig = Figure(figsize=(5, 4), dpi=100)
        nx.draw(self.G, with_labels=True, font_weight='bold')
        nx.draw_shell(self.G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')


    def convert_to_dict(self, text):
        # Initialize an empty dictionary
        result = {}
    
        # Split the text by lines
        lines = text.splitlines()
    
        for line in lines:
            # Split each line by ":"
            key, value = line.split(":")
        
            # Convert the key to an integer and the value to a list of integers
            result[int(key)] = list(map(int, value.split()))
    
        return result

    def dictIntoGraph(self, dic):
        nodes = list(dic.keys())
        edges = []
        print(dic)
        k = 0
        for v in dic.values():
            for i in range(len(v)):
                edges.append((k, v[i]))
            k += 1
        return nodes, edges

# COPIED FROM GITHUB TO TURN ADJECENCY LIST INTO A DICT WHICH CAN BE USED


# Example input
text = """1: 4 5 6
2: 4 5 6
3: 4 5 6
4: 1 2 3 5 6
5: 1 2 3 4 6
6: 1 2 3 4 5"""



# Convert the input text to a dictionary
#output_dict = convert_to_dict(text)

# Print the result
#print(output_dict)

# Turn dictionary of nodes and edges into a graph (from stack overflow)




        
        
"""        
K = Graph()

nodesList, edgesList, = dictIntoGraph(output_dict)

print(nodesList, edgesList)

K.newLists(nodesList, edgesList)

K.updateGraph


K.updateGraph()

print(K)

"""

#K.generatePLTFromGraph
""" 
G = nx.complete_graph(5)

nx.draw(G)

plt.plot()


fig = plt.figure(figsize=(5, 4), dpi=100)
G = nx.petersen_graph()
nx.draw(G, with_labels=True, font_weight='bold')

# From stack overflow
root = tk.Tk()

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

plot_widget.grid(row=0, column=0)
root.mainloop()
 """