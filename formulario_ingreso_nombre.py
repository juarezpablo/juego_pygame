import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from boton_pausa import Pause_Boton
from gui_caja_texto import Caja_texto
import sqlite3

from gui_textbox_2 import TextBox_2

class Formulario_ingreso_alias(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        self.surface=pygame.image.load(imagen_background)
        self.surface= pygame.transform.scale(self.surface,(w,h))
        self.widget_titulo=Widget(self.surface,0,0,w,200,None,1,PATH_IMAGE+"gui/jungle/you_win/header.png")
        self.widget_titulo.surface=pygame.transform.scale(self.widget_titulo.surface,(w,200))
       # self.widget_tabla=Widget(self.surface,300,200,400,400,None,1,PATH_IMAGE+"gui/jungle/pause/bg.png")
        self.widget_nombre=Caja_texto(self.surface,50,200,w/2,100,None,"Name","Comic sans",C_NEGRO,50)
        x_master=x
        y_master=y
        self.boton_continuar=Pause_Boton(self.surface,w/4,350,50,30,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","    CONTINUAR","Comic Sans",C_PINK,30,self.continuar,"form_rank",x_master,y_master)
        
        self.txt1 = TextBox_2(master=self,x=50,y=200,w=w-100,h=70,color_background=None,color_border=None,image_background=PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png",text="Ingresa tu nombre",font="Verdana",font_size=30,font_color=C_NEGRO)
       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_continuar]
        self.lista_widgets=[self.widget_titulo]

        self.lineas=0
        self.caracteres=[]
        self.texto=""
        self.bandera_crear_db=0

        self.score_player=0
        self.vidas_player=0
        self.tiempo_player=0.00

        self.bandera_leer=0

    def crear_db_ranking(self):
        if self.bandera_crear_db==0:
            with sqlite3.connect("sqlite/bd_btf.db") as conexion:
                try:
                    sentencia = ''' create  table personajes
                                    (
                                            id integer primary key autoincrement,
                                            nombre text,
                                            score int,
                                            time real
                                    )
                                '''
                    conexion.execute(sentencia)
                    print("Se creo la tabla personajes")                       
                except sqlite3.OperationalError:
                    print("La tabla personajes ya existe")
            self.bandera_crear_db=1        

    def continuar(self,parametro):
        self.insertar_datos_db()
        self.set_active(parametro)
            
    def insertar_datos_db(self):
        self.texto=self.txt1._text
        mensaje=("{0}".format(self.texto))
        with sqlite3.connect("sqlite/bd_btf.db") as conexion:
            try:
                conexion.execute("insert into personajes(nombre,score,time) values (?,?,?)", (mensaje,self.score_player,self.tiempo_player))
               
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")   
        
  #  def atras(self,parametro):
    ##    self.set_active(parametro)
    def extraer_texto(self,lista_eventos):
        
        for evento in lista_eventos:
            if evento.type== pygame.KEYDOWN:               
                if evento.key== pygame.K_BACKSPACE:
                    largo=len(self.texto)
                    #self.texto=self.texto[0:(largo-1)]
                    self.texto=self.texto[:-1] 
                else:
                    self.texto+=evento.unicode    
        #print(self.texto)
        
        

    def update(self,delta_ms,lista_eventos,player_1):
        self.score_player=player_1.score
        self.vidas_player=player_1.vidas
        self.tiempo_player=player_1.tiempo_de_juego
        for boton in self.lista_botones:
            boton.update(delta_ms,lista_eventos)
            
        for widget in self.lista_widgets:
            widget.update()
        self.extraer_texto(lista_eventos)   
        self.widget_nombre.update(delta_ms,self.texto)   
        self.txt1.update(lista_eventos)

    def draw(self):
        super().draw()
        for boton in self.lista_botones:
            boton.draw()             
        for widget in self.lista_widgets:
            widget.draw()   
        self.widget_nombre.draw()     
            #print("boton: x:{0} y: {1}".format(boton.rectangulo.x,boton.rectangulo.y))
        self.txt1.draw()