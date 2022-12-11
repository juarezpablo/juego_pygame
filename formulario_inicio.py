import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton

class Formulario_inicio(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
       # self.surface=pygame.image.load(imagen_background)
   
        self.boton_elegir_niveles=Boton(self.surface,400,300,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","   JUGAR","Comic Sans",C_PINK,30,self.activar_formulario,"form_level_select")
        self.boton_settings=Boton(self.surface,(w/2),300,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","   SETTINGS","Comic Sans",C_PINK,30,self.activar_formulario,"form_settings")

    def activar_formulario(self,parametro):
        self.set_active(parametro)

    def update(self,delta_ms,lista_eventos):
        self.boton_elegir_niveles.update(delta_ms,lista_eventos)
        self.boton_settings.update(delta_ms,lista_eventos)

    def draw(self):
        super().draw()
        self.boton_elegir_niveles.draw() 
        self.boton_settings.draw()               