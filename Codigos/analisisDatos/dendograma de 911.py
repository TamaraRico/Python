# -*- coding: utf-8 -*-
import pandas as pd
import os
import json
import csv
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
#from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

#del df.index.name

cantAccidentes = {'ems': 0, 'trafico': 0, 'fire': 0}

filtro = pd.read_excel('911.xls')
i = 0
while (i < (filtro.shape[0])):
  tipo = filtro['title'][i]
  if tipo[:4] == 'EMS:':
    cantAccidentes['ems'] += 1
  elif tipo[:5] == 'Fire:':
    cantAccidentes['fire'] += 1
  elif tipo[:8] == 'Traffic:':
    cantAccidentes['trafico'] += 1

  i += 1

tiposA=cantAccidentes.keys()
for i in tiposA:
    print(tiposA[i])
numeros=cantAccidentes.values()
#tabla=[[0,0,0], [0,0,0]]
#Accidentes = ['Emergencia Medica', 'Accidentes de trafico', 'Incendios']




