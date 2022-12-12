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
    def __init__(self,flags,master_surface) :
       
        self.path_nivel_1="niveles_json/nivel_1.json"
        self.path_nivel_2="niveles_json/nivel_2.json"
        self.path_nivel_3="niveles_json/nivel_3.json"
        self.master_surface=master_surface
    #    self.screen=pygame.surface.Surface((ANCHO_VENTANA,ALTO_VENTANA))
        self.stage_1=Nivel(10,self.path_nivel_1,2,1,self.master_surface,False)
        self.stage_2=Nivel(10,self.path_nivel_2,2,2,self.master_surface,False)
        self.stage_3=Nivel(10,self.path_nivel_3,2,3,self.master_surface,False)

        self.lista_niveles=[self.stage_1,self.stage_2,self.stage_3]
    
    def setear_sonido(self,on_off=True):
        if on_off:
            for nivel in self.lista_niveles:
                nivel.setear_sonido(True)
        else:
            for nivel in self.lista_niveles:
                nivel.setear_sonido(False)

   
    def update(self,delta_ms,player_1,lista_eventos):
      #  self.stage_1.update(delta_ms,player_1.municion_list,player_1)
    #   self.gestionar_forms(delta_ms,player_1,lista_eventos)
        pass
    def draw(self,player_1,delta_ms):
        #screen.blit(stage_1.imagen_fondo,stage_1.rect)
        pass
       
       
    
      #  self.stage_1.draw(self.screen,player_1.municion_list)

    