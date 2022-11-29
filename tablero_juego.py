import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player


from stage import Nivel

from gui_widget import Widget, Boton
from gui_barra_progreso import Barra_progresiva
from formulario_inicio import Formulario_inicio
from formulario_nivel import Formulario_level
from formulario_nivel_1 import Formulario_level_1
class Tablero:
    def __init__(self,flags) :
        self.path_nivel_1="C:/Users/Pablo/Desktop/ProgramacionI/game_eventual/niveles_json/nivel_1.json"
        self.screen= pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
        self.stage_1=Nivel(10,self.path_nivel_1,2,self.screen)
        
#        self.formulario_menu=Formulario_inicio("form_menu",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,PATH_IMAGE+"locations/set_bg_05/1_game_background/1_game_background.png",True)

 #       self.formulario_seleccion_nivel=Formulario_level("form_level_select",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,PATH_IMAGE+"locations/set_bg_05/1_game_background/1_game_background.png",False,self.path_nivel_1)
 #       self.form_level_1=Formulario_level_1("form_nivel_1",self.screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"C:/Users/Pablo/Desktop/Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False,self.path_nivel_1)
    '''
    def gestionar_forms(self,delta_ms,player_1,lista_eventos):
        if self.formulario_menu.active:
            self.formulario_menu.update(delta_ms,lista_eventos)
            self.formulario_menu.draw()
        elif self.formulario_seleccion_nivel.active:
            self.formulario_seleccion_nivel.update(delta_ms,lista_eventos,player_1)
            self.formulario_seleccion_nivel.draw()
        elif self.form_level_1.active:
            self.form_level_1.update(delta_ms,lista_eventos,player_1)
            self.form_level_1.draw()  
    '''
    def update(self,delta_ms,player_1,lista_eventos):
        self.stage_1.update(delta_ms,player_1.municion_list,player_1)
    #   self.gestionar_forms(delta_ms,player_1,lista_eventos)

    def draw(self,player_1,delta_ms):
        #screen.blit(stage_1.imagen_fondo,stage_1.rect)

       
        self.screen.blit(self.stage_1.imagen_fondo,self.stage_1.rect)
    
        self.stage_1.draw(self.screen,player_1.municion_list)

    