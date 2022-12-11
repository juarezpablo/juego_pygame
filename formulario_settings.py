import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from boton_pausa import Pause_Boton
from gui_boton_interactivo import Boton_animated

class Formulario_config(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        self.surface=pygame.image.load(imagen_background)
        self.surface= pygame.transform.scale(self.surface,(w,h))
        self.widget_titulo=Widget(self.surface,0,0,w,200,None,1,PATH_IMAGE+"gui/jungle/settings/92.png")
        self.widget_titulo.surface=pygame.transform.scale(self.widget_titulo.surface,(w,200))
       # self.widget_tabla=Widget(self.surface,300,200,400,400,None,1,PATH_IMAGE+"gui/jungle/pause/bg.png")
        x_master=x
        y_master=y
        
        self.boton_audio=Boton_animated(self.surface,w/3,(h/3),40,15,False,PATH_IMAGE+"extras/gui/settings/music_{0}.png",2,self.modif_audio,1,x_master,y_master)
      #  self.boton_menu=Pause_Boton(self.surface,w/4,(h/3)+200,50,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_01.png","MENU","Comic Sans",C_PINK,20,self.continuar,"form_level_select",x_master,y_master)
        self.boton_atras=Pause_Boton(self.surface,w/4,500,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.continuar,"form_menu",x_master,y_master)
       # self.lista_botones=[]
        self.lista_botones=self.lista_botones=[self.boton_atras,self.boton_audio]
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
            #print("boton: x:{0} y: {1}".format(boton.rectangulo.x,boton.rectangulo.y))