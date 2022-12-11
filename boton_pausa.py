import pygame
from constantes import *
from gui_widget import Widget

class Pause_Boton(Widget):
    def __init__(self, master_surface, x, y, w, h, color_background,estado,image_background,text,font,font_color,font_size,on_click,on_click_param,x_master,y_master):
        super().__init__(master_surface, x, y, w, h, color_background,estado,image_background)
        pygame.font.init()
        self.text=text
        self.font_sys=pygame.font.SysFont(font,font_size)
        self.font_color=font_color

        self.on_click=on_click
        self.on_click_param=on_click_param
        self.alto_texto_boton=self.rectangulo.height/3

        
        self.rectangulo.x=x
        self.rectangulo.y=y
        self.rectangulo_de_colision=self.surface.get_rect()
        self.rectangulo_de_colision.x=self.rectangulo.x+x_master
        self.rectangulo_de_colision.y=self.rectangulo.y+y_master



        
    def render(self):
        image_text=self.font_sys.render(self.text,True,self.font_color,self.color_background)
      #  if self.image_background == "no":
       #     self.surface.fill(self.color_background)

        self.surface.blit(image_text,(10,self.alto_texto_boton))
     #   print("{0}".format(image_text.width))

    def update(self,delta_ms,lista_eventos):   

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if (self.rectangulo_de_colision.collidepoint(evento.pos)):
                    print("CLICK BOTON ESTANDAR")
                    self.on_click(self.on_click_param)

        self.render()

   