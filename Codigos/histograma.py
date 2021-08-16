#!/usr/bin/python
# -*- coding: utf-8 -*-
#from pylab import figure
import pylab
import networkx as nx
import pickle
from random import randint

G=nx.read_weighted_edgelist('TIEMPO.CIUDAD.txt', create_using=nx.MultiGraph())

custom_node_color={}
custom_node_color['0'] = 'black'

nx.draw(G, with_labels = True, node_size = [G.degree(i) * 100 for i in G.nodes()])


#Archivo con el dato del promedio del grado de clusterizacion por nodo

avg_node_degree = nx.average_neighbor_degree(G)
vString = str(avg_node_degree)

def make_histogram(aGraph):
	fig = pylab.figure()
	hist = nx.degree_histogram(aGraph)
	pylab.bar(range(len(hist)), hist, align = 'center')
	pylab.xlim((0, len(hist)))
	pylab.xlabel("Ciudad")
	pylab.ylabel("Fecha y hora")
	return fig
def save_histogram(aGraph, filename):
 		fig = make_histogram(aGraph)
 		fig.savefig(filename)

make_histogram(G)
save_histogram(G,"grado2.png")
pylab.show()