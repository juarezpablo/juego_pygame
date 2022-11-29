import pygame
from constantes import *

class Form():
    forms_dict={}
    def __init__(self,name, master_surface, x, y, w, h, color_background, estado, imagen_background,active):
        self.forms_dict[name]=self
        self.active=active
        self.master_surface=master_surface
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color_background=color_background
        #self.surface=pygame.surface.Surface((self.width,self.height))
        self.surface_2=pygame.image.load(imagen_background)
        self.surface_2=pygame.transform.scale(self.surface_2,(w, h))
        self.surface_3=pygame.surface.Surface((self.width,self.height))
        self.surface=self.asignar_imagen()
        self.rectangulo=self.surface.get_rect()
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y
        self.estado=estado

    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True


    def asignar_imagen(self):
        if self.surface_2 == "no":
            self.surface=self.surface_3
        else:
            self.surface=self.surface_2
        return self.surface
                
    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
       
        self.master_surface.blit(self.surface,self.rectangulo)



