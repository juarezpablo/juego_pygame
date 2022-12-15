import pygame
from pygame.locals import *

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

class Gestor_Forms: 
    def __init__(self,screen,tablero) :
        self.screen=screen
        self.tablero=tablero
        self.formulario_menu=Formulario_inicio("form_menu",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/locations/set_bg_05/1_game_background/1_game_background.png",True)

        self.formulario_seleccion_nivel=Formulario_level("form_level_select",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/locations/set_bg_05/1_game_background/1_game_background.png",False)
        self.form_level_1=Formulario_level_1("form_nivel_1",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False)
        self.form_pausa=Formulario_pause("form_pause",self.screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
        self.form_rankings=Formulario_rank("form_rank",self.screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
        self.form_level_2=Formulario_level_2("form_nivel_2",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False)
        self.form_level_3=Formulario_level_3("form_nivel_3",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False)
        self.form_enter_alias=Formulario_ingreso_alias("form_alias",self.screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
        self.form_settings=Formulario_config("form_settings",self.screen,400,100,700,600,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
        self.form_derrota=Formulario_lose("form_derrota",self.screen,500,200,600,500,None,1,"Sprites/images/images/gui/jungle/pause/bg.png",False)
        self.player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=screen)

    def gestionar_formularios(self,delta_ms,player_1,tablero_de_gestion,lista_eventos,keys):
        if self.formulario_menu.active:
            self.formulario_menu.update(delta_ms,lista_eventos)
            self.formulario_menu.draw()
        elif self.formulario_seleccion_nivel.active:
            
            tablero_de_gestion.stage_1.bandera_reset=0
            tablero_de_gestion.stage_2.bandera_reset=0
            tablero_de_gestion.stage_3.bandera_reset=0
            self.player_1.reset=False
            self.formulario_seleccion_nivel.update(delta_ms,lista_eventos)
            self.formulario_seleccion_nivel.draw()

        elif self.form_settings.active:
            if self.form_settings.boton_audio.estado:
                tablero_de_gestion.setear_sonido(on_off=True)
                SET_MUSIC=True
            else:
                tablero_de_gestion.setear_sonido(on_off=False)
                SET_MUSIC=False
            tablero_de_gestion.set_volumen(self.form_settings.delta_volumen)
            self.form_settings.update(delta_ms,lista_eventos)
            self.form_settings.draw()

        elif self.form_level_1.active:
                if self.player_1.reset==False:
                    self.player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=self.screen)
                    self.player_1.reset=True
                tablero_de_gestion.stage_1.reset()
                self.form_level_1.update(delta_ms,lista_eventos,self.player_1,tablero_de_gestion)
                self.form_level_1.draw(delta_ms,self.player_1,tablero_de_gestion)
                self.player_1.events(delta_ms,keys)
        
        elif self.form_level_2.active:
                if self.player_1.reset==False:
                    self.player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=self.screen)
                    self.player_1.reset=True
                self.tablero_de_gestion.stage_2.reset()
                self.form_level_2.update(delta_ms,lista_eventos,self.player_1,tablero_de_gestion)
                self.form_level_2.draw(delta_ms,self.self.player_1,tablero_de_gestion)
                self.player_1.events(delta_ms,keys)
        elif self.form_level_3.active:
                if self.player_1.reset==False:
                    self.player_1 = Player(x=2,y=0,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=200,p_scale=0.2,interval_time_jump=300,tablero=self.screen)
                    self.player_1.reset=True
                tablero_de_gestion.stage_3.reset()
                self.form_level_3.update(delta_ms,lista_eventos,self.player_1,tablero_de_gestion)
                self.form_level_3.draw(delta_ms,self.player_1,tablero_de_gestion)
                self.player_1.events(delta_ms,keys)   

        elif self.form_pausa.active:   
            self.form_pausa.update(delta_ms,lista_eventos,tablero_de_gestion)
            self.form_pausa.draw()        
        elif self.form_derrota.active:
            self.form_derrota.update(delta_ms,lista_eventos,tablero_de_gestion)
            self.form_derrota.draw()
        elif self.form_enter_alias.active:
            self.form_enter_alias.crear_db_ranking()
            self.form_enter_alias.update(delta_ms,lista_eventos,self.player_1)
            self.form_enter_alias.draw()

        elif self.form_rankings.active:
            self.form_rankings.extraer_lista_db()
            self.form_rankings.update(delta_ms,lista_eventos)
            self.form_rankings.draw()      