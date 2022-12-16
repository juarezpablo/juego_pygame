import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from plataforma import Plataform 
from enemy import Enemigo
from proyectil import Bala
from stage import Nivel
from tablero_juego import Tablero




from gestor_formularios import Gestor_Forms
flags = DOUBLEBUF
screen= pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
tablero_de_gestion=Tablero(flags,screen)

pygame.init()
clock = pygame.time.Clock()

#player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=screen)


gestor_forms=Gestor_Forms(screen,tablero_de_gestion)


while True:    
    lista_eventos=pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
    #screen.blit(imagen_fondo,imagen_fondo.get_rect())
    player_1="1"
    gestor_forms.gestionar_formularios(delta_ms,player_1,tablero_de_gestion,lista_eventos,keys)

    
    
    pygame.display.flip()
    
    



    


  



