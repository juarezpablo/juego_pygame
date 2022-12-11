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
        self.boton_continuar=Pause_Boton(self.surface,w/4,340,50,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","CONTINUAR","Comic Sans",C_PINK,20,self.continuar,"form_menu",x_master,y_master)
       # self.boton_atras=Boton(self.surface,w/3,500,100,30,None,1,"C:/Users/Pablo/Desktop/Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.atras,"form_menu")
        self.label_1=Caja_texto(self.surface,15,210,w,30,None,"Name","Comic sans",C_TEXT_RANK_1,30)
        self.label_2=Caja_texto(self.surface,15,250,w,30,None,"Name","Comic sans",C_TEXT_RANK_2,30)
        self.label_3=Caja_texto(self.surface,15,290,w,30,None,"Name","Comic sans",C_TEXT_RANK_3,30)
       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_continuar]
        self.lista_widgets=[self.widget_titulo,self.label_1,self.label_2,self.label_3]
        
        self.lista_rankings=[]
        
        


    def extraer_lista_db(self):
        
            lista=[]
            with sqlite3.connect("sqlite/bd_btf.db") as conexion:
                
                sentencia = "SELECT * FROM personajes ORDER BY score DESC LIMIT 3;"
                cursor=conexion.execute(sentencia)                        
                for fila in cursor:
                    print(fila)
                    lista.append(fila)
                print(lista)    
                
                self.lista_rankings=lista
  
    def filtrar_mensaje(self,index):
        mensaje=""
        nombre=""
        scor=0
        tiempo=0
        lista_a_procesar=self.lista_rankings[:]
        i=0
        if len(lista_a_procesar)> index:
            for item in lista_a_procesar[index]:
                if i==1:
                    nombre=item
                elif i==2:
                    scor = item
                elif i==3:
                    tiempo=item
                i+=1    
        print(nombre,scor,tiempo)    
        mensaje=("  * {0} | Score:{1} | Time:{2}".format(nombre,scor,tiempo))
        print(mensaje)
        return mensaje

    def continuar(self,parametro):
        self.set_active(parametro)
            
        
        
  #  def atras(self,parametro):
    ##    self.set_active(parametro)
    def update(self,delta_ms,lista_eventos):
        
        for boton in self.lista_botones:
            boton.update(delta_ms,lista_eventos)
            
        self.widget_titulo.update() 
        texto=self.filtrar_mensaje(0)   
        self.label_1.update(delta_ms,texto)
        texto=self.filtrar_mensaje(1)
        self.label_2.update(delta_ms,texto)
        texto=self.filtrar_mensaje(2)
        self.label_3.update(delta_ms,texto)
      #  self.boton_nivel_1.update(delta_ms,lista_eventos)
      #  self.boton_atras.update(delta_ms,lista_eventos)

    def draw(self):
        super().draw()
        for boton in self.lista_botones:
            boton.draw()             
        for widget in self.lista_widgets:
            widget.draw()    
            #print("boton: x:{0} y: {1}".format(boton.rectangulo.x,boton.rectangulo.y))
        