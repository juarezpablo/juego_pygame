import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from boton_pausa import Pause_Boton
from gui_boton_interactivo import Boton_animated
from gui_barra_progreso import Barra_progresiva

class Formulario_config(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        self.surface=pygame.image.load(imagen_background)
        self.surface= pygame.transform.scale(self.surface,(w,h))
        self.widget_titulo=Widget(self.surface,0,0,w,200,None,1,"Sprites/images/images/gui/jungle/settings/92.png")
        self.widget_titulo.surface=pygame.transform.scale(self.widget_titulo.surface,(w,200))
       # self.widget_tabla=Widget(self.surface,300,200,400,400,None,1,PATH_IMAGE+"gui/jungle/pause/bg.png")
        x_master=x
        y_master=y
        
        self.boton_audio=Boton_animated(self.surface,w/3,(h/3),40,15,False,"Sprites/images/images/extras/gui/settings/music_{0}.png",2,self.modif_audio,1,x_master,y_master)
      #  self.boton_menu=Pause_Boton(self.surface,w/4,(h/3)+200,50,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","MENU","Comic Sans",C_PINK,20,self.continuar,"form_level_select",x_master,y_master)
        self.boton_atras=Pause_Boton(self.surface,w/3,500,130,40,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.continuar,"form_menu",x_master,y_master)
       # self.lista_botones=[]
        self.delta_volumen=0.3
        self.barra_volumen=Barra_progresiva(self.surface,w/3,450,w/2,25,C_LIGHT_PINK,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Bars/Bar_Background0{0}.png",3,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Bars/Bar_Segment0{0}.png",estilo_punto=2,p_scale=1,valor_a_dibujar=self.delta_volumen,valor_max=9,estado=1)
        self.boton_subir_vol=Pause_Boton(self.surface,130,440,80,30,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/plus.png","","Comic Sans",C_LIGHT_PINK,20,self.set_vol,True,x_master,y_master)
        self.boton_bajar_vol=Pause_Boton(self.surface,30,450+(10),80,30,None,1,"Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/minus.png","","Comic Sans",C_LIGHT_PINK,20,self.set_vol,False,x_master,y_master)
        self.lista_botones=self.lista_botones=[self.boton_atras,self.boton_audio,self.boton_bajar_vol,self.boton_subir_vol]
        self.lista_widgets=[self.widget_titulo]


    def continuar(self,parametro):
        self.set_active(parametro)
            
    def modif_audio(self,parametro):
        if self.boton_audio.estado:
            self.boton_audio.estado=False
        else:
            self.boton_audio.estado=True    
        print(parametro)    
        
  #  def atras(self,parametro):
    ##    self.set_active(parametro)
    def set_vol(self,parametro):
        
        if parametro:
            if self.delta_volumen>=0 and self.delta_volumen<0.9:
                self.delta_volumen+=0.1
        else:
            if self.delta_volumen>=0.1:
                self.delta_volumen+= -0.1    
        S_VOL=self.delta_volumen       
        print(self.delta_volumen)
    def transform(self):
        i=0
        valor=0
        for i in range (10):
            x=self.delta_volumen+(0.9*i)
            if x==i :
                valor=x
                print(i)
            if x>9:
                valor=9
        return valor        

    def update(self,delta_ms,lista_eventos):
        for boton in self.lista_botones:
            boton.update(delta_ms,lista_eventos)
            
        for widget in self.lista_widgets:
            widget.update()    
        valor_volumen=self.transform()
        self.barra_volumen.update(valor_volumen)
      #  self.boton_nivel_1.update(delta_ms,lista_eventos)
      #  self.boton_atras.update(delta_ms,lista_eventos)

    def draw(self):
        super().draw()
        for boton in self.lista_botones:
            boton.draw()             
        for widget in self.lista_widgets:
            widget.draw() 
        self.barra_volumen.draw()       
            #print("boton: x:{0} y: {1}".format(boton.rectangulo.x,boton.rectangulo.y))