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
from formulario_ranking import Formulario_rank
from formulario_nivel_2 import Formulario_level_2
from formulario_ingreso_nombre import Formulario_ingreso_alias
from formulario_settings import Formulario_config
from formulario_nivel_3 import Formulario_level_3
from formulario_derrota import Formulario_lose
flags = DOUBLEBUF
screen= pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
tablero_de_gestion=Tablero(flags,screen)

pygame.init()
clock = pygame.time.Clock()




player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=screen)


formulario_menu=Formulario_inicio("form_menu",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/locations/set_bg_05/1_game_background/1_game_background.png",True)

formulario_seleccion_nivel=Formulario_level("form_level_select",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/locations/set_bg_05/1_game_background/1_game_background.png",False)
form_level_1=Formulario_level_1("form_nivel_1",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False)
form_pausa=Formulario_pause("form_pause",screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
form_rankings=Formulario_rank("form_rank",screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
form_level_2=Formulario_level_2("form_nivel_2",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False)
form_level_3=Formulario_level_3("form_nivel_3",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False)
form_enter_alias=Formulario_ingreso_alias("form_alias",screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
form_settings=Formulario_config("form_settings",screen,400,100,700,600,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
form_derrota=Formulario_lose("form_derrota",screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
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
        
        tablero_de_gestion.stage_1.bandera_reset=0
        tablero_de_gestion.stage_2.bandera_reset=0
        tablero_de_gestion.stage_3.bandera_reset=0
        player_1.reset=False
        
            
        formulario_seleccion_nivel.update(delta_ms,lista_eventos)
        formulario_seleccion_nivel.draw()

    elif form_settings.active:
        if form_settings.boton_audio.estado:
            tablero_de_gestion.setear_sonido(on_off=True)
        else:
            tablero_de_gestion.setear_sonido(on_off=False)
        tablero_de_gestion.set_volumen(form_settings.delta_volumen)
        form_settings.update(delta_ms,lista_eventos)
        form_settings.draw()

    elif form_level_1.active:
            if player_1.reset==False:
                player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=screen)
                player_1.reset=True
            tablero_de_gestion.stage_1.reset()
            form_level_1.update(delta_ms,lista_eventos,player_1,tablero_de_gestion)
            form_level_1.draw(delta_ms,player_1,tablero_de_gestion)
            player_1.events(delta_ms,keys)
    elif form_pausa.active:   
        form_pausa.update(delta_ms,lista_eventos,tablero_de_gestion)
        form_pausa.draw()        
    elif form_derrota.active:
        form_derrota.update(delta_ms,lista_eventos,tablero_de_gestion)
        form_derrota.draw()
    elif form_enter_alias.active:
        form_enter_alias.crear_db_ranking()
        form_enter_alias.update(delta_ms,lista_eventos,player_1)
        form_enter_alias.draw()

    elif form_rankings.active:
        form_rankings.extraer_lista_db()
        form_rankings.update(delta_ms,lista_eventos)
        form_rankings.draw()
    
    elif form_level_2.active:
            if player_1.reset==False:
                player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=screen)
                player_1.reset=True
            tablero_de_gestion.stage_2.reset()
            #player_1.reset()
            form_level_2.update(delta_ms,lista_eventos,player_1,tablero_de_gestion)
            form_level_2.draw(delta_ms,player_1,tablero_de_gestion)
            player_1.events(delta_ms,keys)
    elif form_level_3.active:
            if player_1.reset==False:
                player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=screen)
                player_1.reset=True
            tablero_de_gestion.stage_3.reset()
            #player_1.reset()
            form_level_3.update(delta_ms,lista_eventos,player_1,tablero_de_gestion)
            form_level_3.draw(delta_ms,player_1,tablero_de_gestion)
            player_1.events(delta_ms,keys)       
          

    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    



    


  



