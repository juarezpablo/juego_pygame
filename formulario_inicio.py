import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton

class Formulario_inicio(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
       # self.surface=pygame.image.load(imagen_background)
   
        self.boton_elegir_niveles=Boton(self.surface,w/3,400,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png","NIVELES","Comic Sans",C_PINK,20,self.elegir_niveles,"form_level_select")


    def elegir_niveles(self,parametro):
        self.set_active(parametro)

    def update(self,delta_ms,lista_eventos):
        self.boton_elegir_niveles.update(delta_ms,lista_eventos)

    def draw(self):
        super().draw()
        self.boton_elegir_niveles.draw()                