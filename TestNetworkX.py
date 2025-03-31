import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter as tk

"""
fig = Figure(figsize=(5, 4), dpi=100)
G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
fig.add_subplot(121).plot()
fig.add_subplot(122).plot()

nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.plot()
"""
fig = plt.figure(figsize=(5, 4), dpi=100)
G = nx.petersen_graph()
nx.draw(G, with_labels=True, font_weight='bold')




# From stack overflow
root = tk.Tk()

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()


#fig.canvas.draw()

plot_widget.grid(row=0, column=0)
root.mainloop()