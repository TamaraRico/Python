import pylab
import networkx as nx
import pickle
import matplotlib.pyplot as plt
from random import randint
import scipy
import numpy as np
import math
import pandas as pd
import scipy.cluster.hierarchy as shc

#PATH = "/Users/mariano/Downloads/US_violent_crimes.csv"
#PATH = "/Users/mariano/Downloads/dendo-Hoja-3.csv"
#PATH = "/Users/mariano/Downloads/baseD911.csv"
PATH = "/Users/mariano/Downloads/Datos911.csv"

df = pd.read_csv(PATH)

fig = plt.figure(figsize = (10, 7))

dend = shc.dendrogram(shc.linkage(df[['EMS', 'Traffic', 'Fire']], method = 'ward'), labels = df["Township"].values, color_threshold = 100)

ax = plt.gca()

ax.set_xlabel("County level")
ax.set_ylabel("# of incidents")

ax.tick_params("x", labelsize = 10)
ax.tick_params("y", labelsize = 10)

ax.set_title("Pennsylvania State 911 Calls Incidents by county")
plt.show()
