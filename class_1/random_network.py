# %%
import networkx as nx
import random
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

# In the following script we are going to generate a random graph

## First, we generate 8 random nodes in the horizontal space (0,2) and vertical space (0,4)
random.seed(66)
pos = {i: (random.random() * 2.0, random.random() * 3.0) for i in range(8)}

## Second, we create an edge list by a given probability.
edge_list = []
for node_pair in combinations(list(pos.keys()), 2):
    exist_prob = random.random()
    if exist_prob > 0.7:
        edge_list.append(node_pair)
    else:
        continue

## Now, we can create the graph based on the positions and edge list.

G = nx.from_edgelist(edge_list, create_using=nx.Graph)
fig, ax = plt.subplots()
nx.draw_networkx(G, pos=pos, with_labels=True, ax=ax)
plt.tight_layout()
ax.set_aspect("equal")  # set the equal scale of horizontal and vertical
ax.axis("off")  # remove the frame of the generated figure
#plt.savefig(
#    "/Users/xudongfan/Documents/Courses/CIE500-UrbanNetworks/slides/Unit4/examplegraph.jpg",
#    dpi=300,
#    bbox_inches="tight",
#)

