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
        self.stage_1=Nivel(10,self.path_nivel_1,2,1,self.master_surface,False,"Sprites/images/images/locations/set_bg_05/3_game_background/3_game_background.png")
        self.stage_2=Nivel(10,self.path_nivel_2,2,2,self.master_surface,False,"Sprites/images/images/locations/lvl_2.jpg")
        self.stage_3=Nivel(10,self.path_nivel_3,2,3,self.master_surface,False,"Sprites/images/images/locations/lvl_3.jpg")

        self.lista_niveles=[self.stage_1,self.stage_2,self.stage_3]
        pygame.mixer.music.load("sounds/bits_fondo.mp3")
        pygame.mixer.music.set_volume(0.1) 
        self.bandera_loop_sound=0

    def setear_sonido(self,on_off=True):
        
        for nivel in self.lista_niveles:
            nivel.setear_sonido(on_off)
            
                
        if on_off and self.bandera_loop_sound==0:       
            pygame.mixer.music.play(-1) 
            self.bandera_loop_sound=1
            SET_MUSIC=True
        elif on_off==False:
          #  self.sonido_fondo.stop()
            #self.musica_fondo.play(0)
            pygame.mixer.music.stop()
            self.bandera_loop_sound=0 
            SET_MUSIC=False       
            
    def set_volumen(self,delta_volumen=0.2):
        for nivel in self.lista_niveles:
            nivel.set_volumen(delta_volumen)
            nivel.delta_volumen=delta_volumen
        pygame.mixer.music.set_volume(delta_volumen)    
                  

   
    def update(self,delta_ms,player_1,lista_eventos):

      #  self.stage_1.update(delta_ms,player_1.municion_list,player_1)
    #   self.gestionar_forms(delta_ms,player_1,lista_eventos)
        pass
    def draw(self,player_1,delta_ms):
        #screen.blit(stage_1.imagen_fondo,stage_1.rect)
        pass
       
       
    
      #  self.stage_1.draw(self.screen,player_1.municion_list)

    