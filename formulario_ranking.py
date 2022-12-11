import pygame
from constantes import *
from formularios import Form
from gui_widget import Boton,Widget
from boton_pausa import Pause_Boton
import sqlite3
from gui_caja_texto import Caja_texto

class Formulario_rank(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        self.surface=pygame.image.load(imagen_background)
        self.surface= pygame.transform.scale(self.surface,(w,h))
        self.widget_titulo=Widget(self.surface,0,0,w,200,None,1,PATH_IMAGE+"gui/jungle/rating/header.png")
        self.widget_titulo.surface=pygame.transform.scale(self.widget_titulo.surface,(w,200))
       # self.widget_tabla=Widget(self.surface,300,200,400,400,None,1,PATH_IMAGE+"gui/jungle/pause/bg.png")
        x_master=x
        y_master=y
        self.boton_continuar=Pause_Boton(self.surface,w/4,(h/3)+100,50,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","CONTINUAR","Comic Sans",C_PINK,20,self.continuar,"form_level_select",x_master,y_master)
       # self.boton_atras=Boton(self.surface,w/3,500,100,30,None,1,"C:/Users/Pablo/Desktop/Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.atras,"form_menu")
        self.label_1=Caja_texto(self.surface,20,300,100,30,None,"Name","Comic sans",C_NEGRO,30)
       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_continuar]
        self.lista_widgets=[self.widget_titulo]
        
        self.lista_rankings=[]
        
        


    def extraer_lista_db(self):
        
            lista=[]
            with sqlite3.connect("sqlite/bd_btf.db") as conexion:
                cursor=conexion.execute("SELECT * FROM personajes")
                for fila in cursor:
                    print(fila)
                    lista.append(fila)
                print(lista)    
                
                self.lista_rankings=lista
            
   
    def filtrar_mensaje(self):
        lista_a_procesar=self.lista_rankings

    def continuar(self,parametro):
        self.set_active(parametro)
            
        
        
  #  def atras(self,parametro):
    ##    self.set_active(parametro)
    def update(self,delta_ms,lista_eventos):
        
        for boton in self.lista_botones:
            boton.update(delta_ms,lista_eventos)
            
        for widget in self.lista_widgets:
            widget.update() 
        texto=self.filtrar_mensaje()   
        self.label_1.update(delta_ms,texto)
      #  self.boton_nivel_1.update(delta_ms,lista_eventos)
      #  self.boton_atras.update(delta_ms,lista_eventos)

    def draw(self):
        super().draw()
        for boton in self.lista_botones:
            boton.draw()             
        for widget in self.lista_widgets:
            widget.draw()    
            #print("boton: x:{0} y: {1}".format(boton.rectangulo.x,boton.rectangulo.y))
        self.label_1.draw()