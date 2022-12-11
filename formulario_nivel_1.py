import pygame
from constantes import *
from formularios import Form
from gui_widget import Widget,Boton
from stage import Nivel

class Formulario_level_1(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background, active,path_nivel_1):
        super().__init__(name,master_surface, x, y, w, h, color_background, estado, imagen_background, active)
        
        
        self.bandera_nivel=0
        self.bandera_player_reset=0
   
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
        if self.bandera_player_reset==0:
            player_1.reset()
            self.bandera_player_reset=1

        self.evento_pausa(delta_ms,lista_eventos)
        if self.bandera_nivel ==0:
            tablero_de_gestion.stage_1.active=True
            self.bandera_nivel=1
        if tablero_de_gestion.stage_1.active and tablero_de_gestion.stage_1.derrota==False:
            tablero_de_gestion.stage_1.update(delta_ms,player_1.municion_list,player_1)
            
        elif tablero_de_gestion.stage_1.active==False:
            print("FIN")
            self.bandera_player_reset=0
            self.menu("form_alias")    
        elif tablero_de_gestion.stage_1.derrota:
            self.menu("form_derrota")
        player_1.update(delta_ms,tablero_de_gestion.stage_1.lista_plataformas,tablero_de_gestion) 

    def draw(self,delta_ms,player_1,tablero_de_gestion):
    
        tablero_de_gestion.stage_1.draw(tablero_de_gestion.master_surface,player_1.municion_list)
        player_1.draw(self.master_surface)