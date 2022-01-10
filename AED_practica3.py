# -*- coding: utf-8 -*-
"""
Rico Lopez Tamara Illian 1270673
Grupo 551
Algoritmos y estructuras de datos
Practica 3 Análisis de algoritmos empírico
"""
from funciones import iniciar_eliminacion  

opc=int(input('Tipo de arreglo: \n1=Numeros enteros \n2=Numeros decimales \n3=Oraciones \nopc= '))

if(opc==1):
    arreglo_n=[9,10,22,10,8,9,7,5,6,4,1,10,2,45]
    #arreglo_n=[1,2,5,4,9,7,0,3,5,6,7,4,1,0,2,3,5,9,7,4,5,6,1,2,3,1,2,3,2,5,4,7,8,6,5,1,2,3,9,8,6,5,3,6,3,1]
    # arreglo_n=[9,10,11,12,13,9,10,11,12,13]
    #arreglo_c="Tamara"
    #arreglo_n=[1,1,1,1,1,1,1]
    iniciar_eliminacion(arreglo_n, opc)
elif(opc==2):
    #arreglo_f=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01, 0.02, 0.03, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01, 0.02, 0.03, 2.1, 9.6, 8.3, 45.8, 98.6, 74.012, 0.001, 2.1]
    arreglo_f=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01, 0.02, 0.03, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01, 0.02, 0.03]
    #arreglo_f=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    iniciar_eliminacion(arreglo_f, opc)
elif(opc==3):
    #arreglo_c=(list("Determine	nuevamente los incisos a-g pero ejecutando las funciones en una computadora distinta"))
    #arreglo_c=['s', 'a', 'p', 'i', 't', 'o', ' ', 's', 'a', 'l', 't', 'a', 'r', 'i', 'n', ' ']
    arreglo_c=list("Radiohead es una banda britanica de rock alternativo y art rock originaria de Abingdon-on-Thames, Inglaterra, formada en 1985. Esta integrada por Thom Yorke, Jonny Greenwood, Ed OBrien, Colin Greenwood y Phil Selway.")
    #arreglo_c=list("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    iniciar_eliminacion(arreglo_c, opc)
else:
    print('Esta opcion no esta disponible')
    


