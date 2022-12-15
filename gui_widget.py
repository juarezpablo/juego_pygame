import pygame
from constantes import *

class Widget:
    def __init__(self,master_surface,x,y,w,h,color_background,estado,imagen_background) :
        
        self.master_surface=master_surface
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color_background=color_background
        #self.surface=pygame.surface.Surface((self.width,self.height))
        
        self.surface_2=pygame.image.load(imagen_background)
       
        self.surface_3=pygame.surface.Surface((self.width,self.height))
        self.surface=self.surface_2
        self.rectangulo=self.surface.get_rect()
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y
        self.estado=estado
        
   
    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
       
        self.master_surface.blit(self.surface,self.rectangulo)


class Boton(Widget):
    def __init__(self, master_surface, x, y, w, h, color_background,estado,image_background,text,font,font_color,font_size,on_click,on_click_param):
        super().__init__(master_surface, x, y, w, h, color_background,estado,image_background)
        pygame.font.init()
        self.text=text
        self.font_sys=pygame.font.SysFont(font,font_size)
        self.font_color=font_color

        self.on_click=on_click
        self.on_click_param=on_click_param
        self.alto_texto_boton=self.rectangulo.height/3
        
        
    def render(self):
        image_text=self.font_sys.render(self.text,True,self.font_color,self.color_background)
      #  if self.image_background == "no":
       #     self.surface.fill(self.color_background)
       # ancho_texto_boton=(self.width/2)-((image_text.get_rect().width)/2)
      #  alto_texto_boton=(self.height/2)-((image_text.get_rect().height)/2)
        self.surface.blit(image_text,(10,self.alto_texto_boton))
     #   print("{0}".format(image_text.width))

    def update(self,delta_ms,lista_eventos):   

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if (self.rectangulo.collidepoint(evento.pos)):
                    print("CLICK BOTON ESTANDAR")
                    self.on_click(self.on_click_param)

        self.render()


class Punto:
    def __init__(self,master_surface,x,y,w,h,color_background,estado,imagen_background) :
        
        self.master_surface=master_surface
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color_background=color_background
        #self.surface=pygame.surface.Surface((self.width,self.height))
        
        self.surface=imagen_background
        self.rectangulo=self.surface.get_rect()
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y
        self.estado=estado
        
   
    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
       
        self.master_surface.blit(self.surface,self.rectangulo)
