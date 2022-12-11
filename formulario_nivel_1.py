import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from stage import Nivel

class Formulario_level_1(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active,path_nivel_1):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        #self.surface=pygame.image.load(imagen_background)
        
        #self.boton_pausa=Boton(self.surface,w/3,300,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png","Pause","Comic Sans",C_PINK,20,self.pausa,"form_pause")
        #self.boton_atras=Boton(self.surface,w/3,500,100,30,None,1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png","","Comic Sans",C_LIGHT_PINK,20,self.menu,"form_menu")

       # self.lista_botones=[]
       # self.lista_botones=self.lista_botones=[self.boton_pausa,self.boton_atras]

       # self.stage_1=Nivel(10,path_nivel_1,2,self.master_surface,active)
        self.bandera_nivel=0
   
    def pausa(self,parametro):
        self.set_active(parametro)
            
    def menu(self,parametro):
        self.set_active(parametro)


    def evento_pausa(self,delta_ms,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        self.pausa("form_pause")      
   
    def update(self,delta_ms,lista_eventos,player_1,tablero_de_gestion):
      #  for boton in self.lista_botones:
            #print("botones update")
       #     boton.update(delta_ms,lista_eventos)
      #  self.stage_1.update(delta_ms,player_1.municion_list,player_1)
      #  self.stage_1.draw(self.master_surface,player_1.municion_list)
      #  self.boton_nivel_1.update(delta_ms,lista_eventos)
      #  self.boton_atras.update(delta_ms,lista_eventos)
        self.evento_pausa(delta_ms,lista_eventos)
        if self.bandera_nivel ==0:
            tablero_de_gestion.stage_1.active=True
            self.bandera_nivel=1
        if tablero_de_gestion.stage_1.active and tablero_de_gestion.stage_1.derrota==False:
            tablero_de_gestion.stage_1.update(delta_ms,player_1.municion_list,player_1)
            
        elif tablero_de_gestion.stage_1.active==False:
            print("FIN")
            self.menu("form_alias")    
        elif tablero_de_gestion.stage_1.derrota:
            self.menu("form_derrota")   
    def draw(self,delta_ms,player_1,tablero_de_gestion):
     #   super().draw()
       # for boton in self.lista_botones:
       #     boton.draw()             
        
        tablero_de_gestion.stage_1.draw(tablero_de_gestion.master_surface,player_1.municion_list)