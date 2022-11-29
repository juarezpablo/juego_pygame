import pygame
import sys
from constantes import *
from gui_widget import Widget, Boton
from gui_barra_progreso import Barra_progresiva
from formulario_inicio import Formulario_inicio
from formulario_nivel import Formulario_level
pygame.init()
clock = pygame.time.Clock()
screen= pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), 16)


#def on(parametro):
  #  if parametro == 1:
   #     print("CLICK")


#boton_1=Boton(screen,0,0,200,200,None,1,image_background="C:/Users/Pablo/Desktop/Sprites/images/images/gui/set_gui_01/Pixel_Border/Buttons/Button_M_03.png",text="NIVELES",font="Comic Sans",font_color=C_RED,font_size=18,on_click=on,on_click_param=1)

formulario_menu=Formulario_inicio("form_menu",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,PATH_IMAGE+"locations/set_bg_05/1_game_background/1_game_background.png",True)

formulario_seleccion_nivel=Formulario_level("form_level_select",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,1,PATH_IMAGE+"locations/set_bg_05/1_game_background/1_game_background.png",False)

lista_valores=["coin","coin","","",""]
len(lista_valores)
#barra_vida=Barra_progresiva(screen,800,400,200,25,C_LIGHT_PINK,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Background0{0}.png",1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Segment0{0}.png",estilo_punto=1,p_scale=1,valor_a_dibujar=3,valor_max=6,estado=1)
#self.barra_de_vida=Barra_progresiva(tablero,1200,50,200,25,C_LIGHT_PINK,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Background0{0}.png",1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Segment0{0}.png",estilo_punto=1,p_scale=1,valor_a_dibujar=self.vidas,valor_max=6,estado=1)

print(formulario_seleccion_nivel.forms_dict)
while True:     
    lista_eventos=pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
    if (formulario_menu.active) :
       # print("menu rincipal activo")
        formulario_menu.update(delta_ms,lista_eventos)
        formulario_menu.draw()
    elif (formulario_seleccion_nivel.active):    
      #  print("MenuNivel activo")
        formulario_seleccion_nivel.update(delta_ms,lista_eventos)
        formulario_seleccion_nivel.draw()

 #   boton_1.update(delta_ms,lista_eventos)
 #   boton_1.draw()


    #barra_vida.update(3)
    #barra_vida.draw()

    pygame.display.flip()
    