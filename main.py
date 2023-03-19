import os
os.system('pip install networkx[default]')
os.system('pip install matplotlib')

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from([('s','t'),('s','e'),('s','n'),('t','e'),('e','l'),('e','m'),('l','n'),('m','n'),('l','m'),('l','s')])
options = {
	'node_color': 'blue',
	'node_size': 500,
	'edge_color': 'tab:grey',
	'with_labels': True
}

plt.figure()
nx.draw(g, **options)
plt.show()