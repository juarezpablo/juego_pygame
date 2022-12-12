import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from boton_pausa import Pause_Boton

class Formulario_lose(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        self.surface=pygame.image.load(imagen_background)
        self.surface= pygame.transform.scale(self.surface,(w,h))
        self.widget_titulo=Widget(self.surface,0,0,w,200,None,1,"Sprites/images/images/gui/jungle/you_lose/header.png")
        self.widget_titulo.surface=pygame.transform.scale(self.widget_titulo.surface,(w,200))
       # self.widget_tabla=Widget(self.surface,300,200,400,400,None,1,PATH_IMAGE+"gui/jungle/pause/bg.png")
        x_master=x
        y_master=y
        self.boton_continuar=Pause_Boton(self.surface,w/4,(h/3)+50,50,30,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","CONTINUAR","Comic Sans",C_PINK,20,self.continuar,"form_menu",x_master,y_master)
        

       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_continuar]
        self.lista_widgets=[self.widget_titulo]
        self.tablero=0

    def continuar(self,parametro):
            self.set_active(parametro)
            
        
        
  #  def atras(self,parametro):
    ##    self.set_active(parametro)
    def update(self,delta_ms,lista_eventos,tablero):
        self.tablero=tablero
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
            #print("boton: x:{0} y: {1}".format(boton.rectangulo.x,boton.rectangulo.y))