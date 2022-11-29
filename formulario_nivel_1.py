import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from stage import Nivel

class Formulario_level_1(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active,path_nivel_1):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        #self.surface=pygame.image.load(imagen_background)
        
        self.boton_nivel_1=Boton(self.surface,w/3,300,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png","Nivel 1","Comic Sans",C_PINK,20,self.pausa,1)
        self.boton_atras=Boton(self.surface,w/3,500,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.menu,"form_menu")

       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_nivel_1,self.boton_atras]

       # self.stage_1=Nivel(10,path_nivel_1,2,self.master_surface,active)

   
    def pausa(self,parametro):
        pass
            
    def menu(self,parametro):
        self.set.active(parametro)
   
    def update(self,delta_ms,lista_eventos,player_1):
        for boton in self.lista_botones:
            #print("botones update")
            boton.update(delta_ms,lista_eventos)
      #  self.stage_1.update(delta_ms,player_1.municion_list,player_1)
      #  self.stage_1.draw(self.master_surface,player_1.municion_list)
      #  self.boton_nivel_1.update(delta_ms,lista_eventos)
      #  self.boton_atras.update(delta_ms,lista_eventos)

    def draw(self):
        super().draw()
        for boton in self.lista_botones:
            boton.draw()             