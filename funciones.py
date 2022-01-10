# -*- coding: utf-8 -*-
"""
Rico Lopez Tamara Illian 1270673
Grupo 551
Algoritmos y estructuras de datos
Practica 3 Análisis de algoritmos empírico
"""
from collections import OrderedDict
import numpy as np
import time

def iniciar_eliminacion(arreglo, opc):
    resultado=arreglo[:]
    print('\nEl arreglo es: ', arreglo)
    tic=time.perf_counter()
    arreglo=eliminar_elementos_repetidos(arreglo)
    if(opc==3):
        print('\nEl arreglo es: ', resultado)
        print('\nEl arreglo sin elementos repetidos',de_lista_a_string(arreglo))
        toc=time.perf_counter()
        tiempo=toc-tic
        print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo))
        tic1=time.perf_counter()
        print('\nUsando diccionarios: ', de_lista_a_string(eliminar_con_set(resultado)))
        toc1=time.perf_counter()
        tiempo1=toc1-tic1
        print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo1))
        tic2=time.perf_counter()
        print('\nUsando numpy: ', de_lista_a_string(usando_numpy(resultado)))
        toc2=time.perf_counter()
        tiempo2=toc2-tic2
        print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo2))
    else:
        print('\nEl arreglo es: ', resultado)
        print('\nEl arreglo sin elementos repetidos',arreglo)
        toc=time.perf_counter()
        tiempo=toc-tic
        print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo))
        tic1=time.perf_counter()
        print('\nUsando diccionarios: ', eliminar_con_set(resultado))
        toc1=time.perf_counter()
        tiempo1=toc1-tic1
        print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo1))
        tic2=time.perf_counter()
        print('\nUsando numpy: ', usando_numpy(resultado))
        toc2=time.perf_counter()
        tiempo2=toc2-tic2
        print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo2))


def eliminar_elementos_repetidos(arreglo):
    i=0
    iteraciones=0
    while i in range(len(arreglo)):
        x=arreglo[i]
        j=i+1
        while j<(len(arreglo)):
            print('Es {} igual a {}?'.format(x, arreglo[j]))
            if(x==arreglo[j]):
                print('True')
                arreglo.pop(j)
                #arreglo=arreglo.replace(arreglo[j], '')
                j-=1
            j+=1
            iteraciones+=1
        i+=1
        iteraciones+=1
    print('Iteraciones=', iteraciones)
    print('Fin del arreglo')
    return arreglo

                
def eliminar_con_set(arreglo):
    # list(set(arreglo)) cambia el orden de los elementos del arreglo
    arr=OrderedDict((x, True) for x in arreglo).keys()
    return list(arr)
    
    
def usando_numpy(arreglo):
    lista_aux=np.array(arreglo)
    lista_aux, index=np.unique(lista_aux, return_index=True)
    return lista_aux[index.argsort()]
    
def de_lista_a_string(arreglo):
    string=""
    return string.join(arreglo)

    