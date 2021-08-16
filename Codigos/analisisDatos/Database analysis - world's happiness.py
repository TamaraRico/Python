#!/usr/bin/python
# -*- coding: utf-8 -*-
# from pylab import figure
# from mpl_toolkits.basemap import Basemap

import pylab
import networkx as nx
import pickle
import matplotlib.pyplot as plt
from random import randint
import scipy
import numpy as np
import math
import csv

with open('2019.csv', mode='w') as csv_file:
        reader=csv.DictReader(csv_file)
        line_count = 0
        for row in reader:
                if line_count == 0:
                        print(f'El nombre de las columnas es: {", ".join(row)}')
                        line_count += 1
                print(f'\tEl número {row["ranking"]} es el país {row["pais"]} que tiene {row["coordenadas"]} y una puntuación {row["puntuación"]} que incluye el PIB per capita {row["pib"]} la ayuda social {row["socials"]} y una esperanza de vida de sana {row["evs"]} libertad {row["lib"]}generosidad {row["generosidad"]} y percepción de la corrupción {row["corrupcion"]}.')
                line_count+=1
        print(f'Procesadas {line_count} líneas')

#G = nx.Graph()
# AGEB

#G.add_node('Playas de Rosarito', pos=(1170322, 322032), population=65278, escolaridad=8.8, pea=27850)
#population = nx.get_node_attributes(G, 'population')
#escolaridad = nx.get_node_attributes(G, 'escolaridad')
#pea = nx.get_node_attributes(G, 'pea')
#G.nodes(data=True)
#node_color = [float(escolaridad[v]) for v in G]
#node_size = [float(population[v]) for v in G]
#
#cmap = plt.cm.rainbow

#nx.draw(G, nx.get_node_attributes(G, 'pos'), font_size=12, with_labels=True, node_size=node_size,
#        node_color=node_color, edge_cmap=cmap)
#sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(node_color))
#sm._A = []
#plt.colorbar(sm)
#plt.show()









