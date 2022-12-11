import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from stage import Nivel
from formulario_nivel_1 import Formulario_level_1

class Formulario_level(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        #self.surface=pygame.image.load(imagen_background)
        self.widget_titulo=Widget(self.surface,w/4,50,w/2,200,None,1,PATH_IMAGE+"gui/jungle/level_select/header.png")
        self.widget_titulo.surface=pygame.transform.scale(self.widget_titulo.surface,(w/2,200))
        self.boton_nivel_1=Boton(self.surface,w/3,300,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","Nivel 1","Comic Sans",C_PINK,20,self.elegir_nivel,"form_nivel_1")
        self.boton_atras=Boton(self.surface,w/3,600,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.atras,"form_menu")
        self.boton_nivel_2=Boton(self.surface,w/3,450,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","Nivel 2","Comic Sans",C_PINK,20,self.elegir_nivel,"form_nivel_2")
       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_nivel_1,self.boton_atras,self.boton_nivel_2]
      #  self.form_level_1=Formulario_level_1("form_nivel_1",self.master_surface,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,"C:/Users/Pablo/Desktop/Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",False,path_nivel_1)
        

    def elegir_nivel(self,parametro):
        
        self.set_active(parametro)
            
        
    def atras(self,parametro):
        print("ATRAS")
        self.set_active(parametro)

    def update(self,delta_ms,lista_eventos,player_1):
        for boton in self.lista_botones:
            #print("botones update")
            boton.update(delta_ms,lista_eventos)
    #    if self.form_level_1.active:
       #     self.form_level_1.update(delta_ms,lista_eventos,player_1)
      #      self.form_level_1.draw()
        
      #  self.boton_nivel_1.update(delta_ms,lista_eventos)
      #  self.boton_atras.update(delta_ms,lista_eventos)
            self.widget_titulo.update()
    def draw(self):
        super().draw()
        for boton in self.lista_botones:
            boton.draw()             
        self.widget_titulo.draw()    