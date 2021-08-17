#Código de un juego en el que una figura debe esquivar a otras figuras que caen de la parte superior de la pantalla
#    Se va incrementando de nivel a medida de los cuadros caen con una velocidad mayor
#

import sys
import random
import pygame
#pygame = crea un ciclo que no se cierra hasta que el juego se marca como game over 

pygame.init()

#inicializamos las variables para e tamaño de la pantalla con el juego 
#asi es mas facil cambiar el tamaño de la altura y el ancho

altura=600
ancho=800

#inicializar variables para hacer que el codigo sea entendible

pos_tam=50
pos_fig=[ancho/2,altura-2*pos_tam]

#cuadrados enemigos 
rect_arriba_tam=50
rect_arriba_pos=[random.randint(0,ancho-rect_arriba_tam),0] #cero es desde arriba, no se va ver hasta que empiece, y random para que sea desde cualquier lugar
velocidad=10
lista_enemies=[rect_arriba_pos]

azul=(27,161,226)
negro=(0,0,0)
amarillo=(227,200,0)
magenta=(216,0,115) #tupla

pantalla=pygame.display.set_mode((ancho,altura))#tamaño en pixeles

#condiciones para ganar
game_over=False
fuente = pygame.font.SysFont("monospace", 35)
puntuacion=0

#frames per second rate = que tan rapido se mueve el juego
tiempo=pygame.time.Clock()

#funcion para ajustar la velocidad del juego de forma progresiva
def nivel_juego(puntuacion, velocidad):
	if puntuacion < 20:
		velocidad= 5
	elif puntuacion < 40:
		velocidad= 8
	elif puntuacion < 60:
		velocidad= 12
	else:
		velocidad= 15
	return velocidad
	# SPEED = score/5 + 1

#funcion para que caigan mas de un cuadro al mismo tiempo
def drop_cuadros(lista_enemies):
    #queremos que max haya 10 cuadros enemigos en el juego
    cuadros_lento=random.random()
    if len(lista_enemies)<10 and cuadros_lento<0.1:
        pos_x= random.randint(0,ancho-rect_arriba_tam)
        pos_y=0
        lista_enemies.append([pos_x, pos_y])

#funcion para dibujar todos los enemigos cuadros que van aparecer
def dibujar_enemigos(lista_enemies):
    for rect_arriba_pos in lista_enemies:
        pygame.draw.rect(pantalla, amarillo, (rect_arriba_pos[0], rect_arriba_pos[1], rect_arriba_tam, rect_arriba_tam))

#funcion para que los cuadros se muevan hacia abajo 
def mov_cuadros(lista_enemies, puntuacion):
    for idx, rect_arriba_pos in enumerate(lista_enemies):
        if rect_arriba_pos[1] >= 0 and rect_arriba_pos[1] < altura:
            rect_arriba_pos[1] += velocidad
        else:
            #se COMENTA porque esta en la funcion drop_cuadrps
            #rect_arriba_pos[0] = random.randint(0, ancho-rect_arriba_tam)
            #rect_arriba_pos[1] = 0

            #para quitar el cuadro de la lista si esta fuera de la pantalla
            lista_enemies.pop(idx)
            puntuacion+=1
    return puntuacion

#funcion para ver cuando choquen los cuadros y pierdes
def choques_cuadros(pos_fig, rect_arriba_pos):
    player_x=pos_fig[0]
    player_y=pos_fig[1]

    enemy_x=rect_arriba_pos[0]
    enemy_y=rect_arriba_pos[1]

    if((player_x >= enemy_x and player_x < (enemy_x+rect_arriba_tam))or(enemy_x >= player_x and enemy_x < (player_x+pos_tam))):
        if((player_y >= enemy_y and player_y < (enemy_y+rect_arriba_tam))or(enemy_y >= player_y and enemy_y < (player_y+pos_tam))):
            return True
    return False

#funcion para checar cuando el cuadrado choque con algunos de los 10 cuadros enemigos
def checar_choques(lista_enemies, pos_fig):
    for rect_arriba_pos in lista_enemies:
        if choques_cuadros(pos_fig, rect_arriba_pos):
            return True
    return False

#JUEGO
while not game_over:
    for event in pygame.event.get():
        #event no es una variable, es parte de la biblioteca
        if (event.type == pygame.QUIT):
            #sentencias reservadas
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            #para escribir menos y hacer mas bonito
            x=pos_fig[0]
            y=pos_fig[1]
            if (event.key == pygame.K_LEFT):
                x-=pos_tam
            elif (event.key == pygame.K_RIGHT):
                x+=pos_tam
            pos_fig=[x,y]

    pantalla.fill((negro))

    #cambia la posicion de la que salen los cuadros que debemos esquivar
    #REMOVED funcion mov_ cuadros = if rect_arriba_pos[1]>=0 and rect_arriba_pos[1]<altura:
    #    rect_arriba_pos[1]+=velocidad
    #else:
    #    rect_arriba_pos[0]=random.randint(0, ancho-rect_arriba_tam)
    #    rect_arriba_pos[1]=0
    
    #REMOVED funcion checar_choques = if choques_cuadros(pos_fig, rect_arriba_pos):
    #    game_over=True
    #    break

    #llamadas a todas las funciones que se hicieron
    drop_cuadros(lista_enemies)
    puntuacion = mov_cuadros(lista_enemies, puntuacion)
    velocidad = nivel_juego(puntuacion, velocidad)

    #letras que dicen puntuacion y diseño
    texto ="Puntuación:" + str(puntuacion)
    label= fuente.render(texto, 1, azul)
    pantalla.blit(label, (ancho-200, altura-40))

    #para revisar si se sigue en el juego
    if checar_choques(lista_enemies, pos_fig):
        game_over=True
        break
    dibujar_enemigos(lista_enemies)

    #hacer las formas que existen en el juego fuera de las condiciones para ganar pero dentro del juego
    pygame.draw.rect(pantalla, magenta, (pos_fig[0], pos_fig[1], pos_tam, pos_tam))
                    #1) donde? en la pantalla
                    #2) color = rgb color code
                    #3) dimensiones = 2 en la pantalla, 2 del cuadrado
    #REMOVED (funcion dibujar) pygame.draw.rect(pantalla, amarillo, (rect_arriba_pos[0], rect_arriba_pos[1], rect_arriba_tam, rect_arriba_tam))

    tiempo.tick(30)
    pygame.display.update() #actualiza las pantallas con las modificaciones que hemos hecho



