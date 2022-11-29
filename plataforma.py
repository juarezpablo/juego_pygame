import pygame
from constantes import *
from auxiliar import Auxiliar


#C:\Users\Pablo\Desktop\Sprites\images\images\tileset\graveyard\Tiles
class Plataform:
    def __init__(self, x, y,width, height,  type=1, path=PATH_IMAGE , cant_fotogramas=10 ,naturaleza ="solida"):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.naturaleza = naturaleza
        self.terreno_colision_rect=pygame.Rect(self.rect)
        self.terreno_colision_rect.width=self.rect.width-5
        self.terreno_colision_rect.x = self.rect.x +5
        self.terreno_colision_rect.height= self.rect.height-5
        

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
           # pygame.draw.rect(screen,color=C_RED,rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color =(255,100,255),rect=self.terreno_colision_rect)
        