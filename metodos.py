# -*- coding: utf-8 -*-
"""
Rico Lopez Tamara Illian 1270673
Grupo 551
Algoritmos y estructuras de datos
Practica 4 Análisis de algoritmos empírico y recursión
"""

def preparar_cadena(cadena):
    cadena=cadena.lower()
    cadena=cadena.replace('.', '').replace(',', '')
    arreglo=cadena.split()
    arreglo.sort()
    return arreglo

def busqueda_binaria_recursiva(llave, izq, der, arreglo, iteraciones):
    centro=int((izq+der)/2)
    iteraciones+=1
    print('\nLlave: {} Posicion_Arreglo: {}'.format(llave, arreglo[centro]))
    print('izq: {} der: {} centro: {}'.format(izq, der, centro))
    if(izq>der):
        return -1, iteraciones
    elif(llave==arreglo[centro]):
        return centro, iteraciones
    elif(llave>arreglo[centro]):
        return busqueda_binaria_recursiva(llave, centro+1, der, arreglo, iteraciones)
    elif(llave<arreglo[centro]):
        return busqueda_binaria_recursiva(llave, izq, centro-1, arreglo, iteraciones)


def busqueda_binaria_iterativa(llave, arreglo):
    izq, der=0, len(arreglo)-1
    iteraciones=0
    while(izq<=der):
        iteraciones+=1
        centro=(izq+der)//2
        print('\nLlave: {} Posicion_Arreglo: {}'.format(llave, arreglo[centro]))
        print('izq: {} der: {} centro: {}'.format(izq, der, centro))
        if(llave==arreglo[centro]):
            return centro, iteraciones
        elif(llave>arreglo[centro]):
            izq=centro+1
        else:
            der=centro-1
    return -1, iteraciones
