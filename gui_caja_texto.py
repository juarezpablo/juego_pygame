import pygame
from constantes import *
from gui_widget import Widget

class Caja_texto:
    def __init__(self, master_surface, x, y, w, h, color_background,text,font,font_color,font_size):
        pygame.font.init()
        self.master_surface=master_surface
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color_background=color_background
        #self.surface=pygame.surface.Surface((self.width,self.height))
        
        
       
        
        self.surface=pygame.surface.Surface((self.width,self.height))
        self.rectangulo=self.surface.get_rect()
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y
        
    
        self.text=text
        self.font_sys=pygame.font.SysFont(font,font_size)
        self.font_color=font_color

     
        self.alto_texto_boton=self.rectangulo.height/3
        self.image_text=self.render(self.text)

        
    def render(self,texto):
        self.image_text=self.font_sys.render("{0}".format(texto),True,self.font_color,self.color_background)
      

      #  self.surface.blit(image_text,(0,self.alto_texto_boton))
        #print("TEXTO: {0}".format(texto))

    def update(self,delta_ms,texto):   

        
        self.render(texto)

    def draw(self):
       
        self.master_surface.blit(self.image_text,self.rectangulo)
