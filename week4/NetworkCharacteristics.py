#%%

import networkx as nx
import random
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

## First, we generate 9 random nodes in the horizontal space (0,2) and vertical space (0,4)
random.seed(66)
pos = {i: (random.random() * 1.0, random.random() * 6.0) for i in range(9)}
pos

## we create an edge list by distance.
edge_list1 = []
for node_pair in combinations(list(pos.keys()), 2):
    node_dist = np.sqrt((pos[node_pair[0]][0]-pos[node_pair[1]][0])**2+(pos[node_pair[0]][1]-pos[node_pair[1]][1])**2)
    if node_dist < 2:
        edge_list1.append(node_pair)
    else:
        continue

##Visualize the network
G = nx.from_edgelist(edge_list1, create_using=nx.DiGraph) # DiGraph is a directed graph
fig, ax = plt.subplots()
nx.draw_networkx(G, pos=pos, with_labels=True, node_size=400,linewidths=.5, ax=ax)
plt.tight_layout()
#ax.set_aspect("equal")  # set the equal scale of horizontal and vertical
ax.axis("off")  # remove the frame of the generated figure
#plt.savefig(
#    "/Users/rileybla/Desktop/CIE500_SP2025/examplegraph.jpg",
#    dpi=300,
#    bbox_inches="tight",
#)
plt.show()
# %%
## Calculate Network Charcteristics
print(
    f"The adjancency matrix of G is \n {nx.adjacency_matrix(G, nodelist=list(range(1,9))).toarray()}"
)
# get the topological sort order of the graph.
sorted_order = list(nx.topological_sort(G))
print(f"the sorted order is {sorted_order}")

print(
    f"the length of sorted order is {len(sorted_order)}\n the total number of nodes is {len(G.nodes())}"
)

# Finding the shortest path

# Use Bellman-Ford to find the shortest path from node 1 to node 6
try:
    # Get the shortest path from node 1 to all other nodes
    path = nx.single_source_bellman_ford_path(G, source=1)

    # If node 6 is in the paths, print the path
    if 6 in path:
        print(f"The shortest path from node 1 to node 6 is: {path[6]}")
    else:
        print("There is no path from node 1 to node 6.")
except nx.NetworkXUnreachable:
    print("The graph is not connected between node 1 and node 6.")

#Find the diameter of the network
try:
    diameter = nx.diameter(G.to_undirected())  # Convert to undirected to handle diameter computation
    print("Diameter of the network:", diameter)
except nx.NetworkXError:
    print("Graph is not connected, diameter is not defined.")

# %%
# Betweenness centrality

node_central = nx.betweenness_centrality(G)

fig, ax = plt.subplots(figsize=(5, 8))

nx.draw_networkx(
    G,
    pos=pos,
    with_labels=True,
    node_color=list(node_central.values()), # make heat scale red to yellow with increasing conectedness
    node_size=400,
    font_size=16,
)
ax.axis("off")  # remove the frame of the generated figure
#plt.savefig(
#    "/Users/rileybla/Desktop/CIE500_SP2025/betweenness.jpg",
#    dpi=600,
#    bbox_inches="tight",
#)
plt.show()

#Closeness centrality

node_clossness = nx.closeness_centrality(G)

fig, ax = plt.subplots(figsize=(5, 8))

nx.draw_networkx(
    G,
    pos=pos,
    with_labels=True,
    node_color=list(node_clossness.values()),
    node_size=400,
    font_size=16,
)
ax.axis("off")  # remove the frame of the generated figure
plt.show()
# %%Macroscopic analysis