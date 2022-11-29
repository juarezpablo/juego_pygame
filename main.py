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


from formulario_inicio import Formulario_inicio
from formulario_nivel import Formulario_level
from formulario_nivel_1 import Formulario_level_1
from formulario_pausa import Formulario_pause


path_nivel_1="C:/Users/Pablo/Desktop/ProgramacionI/game_eventual/niveles_json/nivel_1.json"
flags = DOUBLEBUF
screen= pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
tablero_de_gestion=Tablero(flags)

pygame.init()
clock = pygame.time.Clock()



#imagen_fondo = pygame.image.load(PATH_IMAGE+"locations/set_bg_05/3_game_background/3_game_background.png").convert()

#imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=tablero_de_gestion.screen)

#stage_1=Nivel(10,2)
formulario_menu=Formulario_inicio("form_menu",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,PATH_IMAGE+"locations/set_bg_05/1_game_background/1_game_background.png",True)

formulario_seleccion_nivel=Formulario_level("form_level_select",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,PATH_IMAGE+"locations/set_bg_05/1_game_background/1_game_background.png",False)
form_level_1=Formulario_level_1("form_nivel_1",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False,path_nivel_1)
form_pausa=Formulario_pause("form_pause",screen,300,200,400,500,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Frames/Frames_Menu06_b.png",False)


while True:    
    lista_eventos=pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
    #screen.blit(imagen_fondo,imagen_fondo.get_rect())
    if formulario_menu.active:
        formulario_menu.update(delta_ms,lista_eventos)
        formulario_menu.draw()
    elif formulario_seleccion_nivel.active:
        formulario_seleccion_nivel.update(delta_ms,lista_eventos,player_1)
        formulario_seleccion_nivel.draw()
    elif form_level_1.active:
          #  form_level_1.update(delta_ms,lista_eventos,player_1)
            tablero_de_gestion.update(delta_ms,player_1,lista_eventos)
            tablero_de_gestion.draw(player_1,delta_ms)
            player_1.events(delta_ms,keys)
            player_1.update(delta_ms,tablero_de_gestion.stage_1.lista_plataformas)
            player_1.draw(tablero_de_gestion.screen)
        #    form_level_1.draw()  
    #screen.blit(tablero_de_gestion.stage_1.imagen_fondo,tablero_de_gestion.stage_1.rect)
    
   # 
    #stage_1.update(delta_ms,player_1.municion_list,player_1)
    #stage_1.draw(screen,player_1.municion_list)
  #  
   
    #for enemigo in enemie_list:
     #   enemigo.automatize(delta_ms)
     #   enemigo.update(delta_ms,plataform_list,player_1.municion_list)
     #   enemigo.draw(screen)
    
    
        



    
    #print(delta_ms)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    #print(delta_ms)



    


  



