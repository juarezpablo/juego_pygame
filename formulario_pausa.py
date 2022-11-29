import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton

class Formulario_pause(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        #self.surface=pygame.image.load(imagen_background)
        self.widget_titulo=Widget(self.surface,100,0,200,30,None,1,PATH_IMAGE+"gui/jungle/pause/header.png")
        self.widget_tabla=Widget(self.surface,80,0,160,400,None,1,PATH_IMAGE+"gui/jungle/pause/bg.png")
        self.boton_continuar=Boton(self.surface,w/3,300,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png","Nivel 1","Comic Sans",C_PINK,20,self.continuar,"form_nivel_1")
       # self.boton_atras=Boton(self.surface,w/3,500,100,30,None,1,"C:/Users/Pablo/Desktop/Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.atras,"form_menu")

       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_continuar]
        self.lista_widgets=[self.widget_tabla,self.widget_titulo]
    def continuar(self,parametro):
        self.set_active(parametro)
            
        
        
  #  def atras(self,parametro):
    ##    self.set_active(parametro)
    def update(self,delta_ms,lista_eventos):
        for boton in self.lista_botones:
            boton.update(delta_ms,lista_eventos)
            
        for widget in self.lista_widgets:
            widget.update()    
        
      #  self.boton_nivel_1.update(delta_ms,lista_eventos)
      #  self.boton_atras.update(delta_ms,lista_eventos)

    def draw(self):
        super().draw()
        for boton in self.lista_botones:
            boton.draw()             
        for widget in self.lista_widgets:
            widget.draw()    