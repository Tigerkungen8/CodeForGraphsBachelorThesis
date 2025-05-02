import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import Graphs as G

############# TEST
#import tkinter as tk
##################


global fig
fig = Figure(figsize=(5, 4), dpi=100)


text = """1: 4 5 6
2: 4 5 6
3: 4 5 6
4: 1 2 3 5 6
5: 1 2 3 4 6
6: 1 2 3 4 5"""

        
Gr = nx.complete_graph(5)
print(Gr)

        
        
K = G.Graph()

K.initiateGraph()

output_dict = K.convert_to_dict(text)

print(output_dict)


pos = nx.spring_layout(K.G, seed=7)
nx.draw_networkx_nodes(K.G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=K.edgeList, width=6)


nodesList, edgesList, = K.dictIntoGraph(output_dict)

print(nodesList, edgesList)

K.newLists(nodesList, edgesList)

K.updateGraph


K.updateGraph()

print(K)

K.generatePLTFromGraph

""" 
G = nx.complete_graph(5)

nx.draw(G)

plt.plot()
plt.show()
"""
""" 
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