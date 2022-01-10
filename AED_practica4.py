# -*- coding: utf-8 -*-
"""
Rico Lopez Tamara Illian 1270673
Grupo 551
Algoritmos y estructuras de datos
Practica 4 Análisis de algoritmos empírico y recursión
"""
from metodos import preparar_cadena, busqueda_binaria_iterativa, busqueda_binaria_recursiva
import time

#cadena="The Metropolitan Museum of Art presents over 5,000 years of art from around the world for everyone to experience and enjoy. The Museum lives in New York City"
#cadena="El Museo Metropolitano de Arte es uno de los museos de arte más destacados del mundo. Situado en el distrito de Manhattan, en la ciudad de Nueva York, abrió sus puertas el 20 de febrero de 1872. La colección del museo es de más de dos millones de obras de arte de todo el mundo"
# print("Cadena de caracteres: \n", cadena)
# cadena=preparar_cadena(cadena)
arreglo=[1,2,3,4,5,6,7,8, 9, 10, 11]

# #busqueda='el'
# busqueda= 'everyone'
# print('\nElemento a buscar: ', busqueda)
# buscar=busqueda.lower()
buscar=11

inicio=time.perf_counter()
print('\nBusqueda binaria recursiva---------------------------')
indice, iteraciones = busqueda_binaria_recursiva(buscar, 0, len(arreglo)-1, arreglo, 0)
print('\nBusqueda binaria recursiva')
print("El elemento {} está en el índice {}".format(buscar, indice))
print('Numero de iteraciones: ', iteraciones)
fin=time.perf_counter()
tiempo=fin-inicio
print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo))

inicio=time.perf_counter()
print('\nBusqueda binaria iterativa---------------------------')
indice, iteraciones = busqueda_binaria_iterativa(buscar, arreglo)
print('\nBusqueda binaria iterativa')
print("El elemento {} está en el índice {}".format(buscar, indice))
print('Numero de iteraciones: ', iteraciones)
fin=time.perf_counter()
tiempo=fin-inicio
print('Tiempo en ejecutar el código : {:0.4f} segundos'.format(tiempo))



