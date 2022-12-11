import pygame
from constantes import *
from auxiliar import Auxiliar

class Boton_animated:
    def __init__(self,master_surface,x,y,w,h,estado,path_image,cant_fotogramas,on_click,on_click_param,x_master,y_master) :
        self.image_sprite= Auxiliar.getSurfaceFromSeparateFiles(path_image,cant_fotogramas,flip=True)
        self.frame=0
        self.animation=self.image_sprite
        self.surface=self.animation[self.frame]
        
        self.master_surface=master_surface
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        
        
        self.rectangulo=self.surface.get_rect()
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y
        
        self.estado=estado
        self.on_click=on_click
        self.on_click_param=on_click_param
        self.colision_rect=pygame.Rect(self.rectangulo)
        self.colision_rect.x=x_master+self.x
        self.colision_rect.y=y_master+self.y
        

    def do_animation(self):
        if self.estado:
            self.frame=1
            print("Cambiar a frame1")
        else:
            self.frame=0   
            print("Cambiara aframe 0")

    def update(self,delta_ms,lista_eventos):   
        self.do_animation()
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if (self.colision_rect.collidepoint(evento.pos)):
                    print("RECT.x{0}-- POS.mouse: {1}".format(self.rectangulo.x,evento.pos))
                    print("CLICK BOTON ESTANDAR")
                    self.on_click(self.on_click_param)

    def draw(self):
        self.surface=self.animation[self.frame]
        self.master_surface.blit(self.surface,self.rectangulo)
      #  pygame.draw.rect(self.master_surface,color=C_PINK,rect=self.rectangulo)

