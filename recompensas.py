import pygame
from constantes import *
from auxiliar import Auxiliar

class Botin:
    def __init__(self,x,y,path,width, height,cant_fotogramas,type,tipo_imagen,naturaleza,estado=1,frame_rate_ms=100):
        #self.image_list = self.asignar_imagen(path,cant_fotogramas,width,height)
        self.image_list=Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=False,w=width,h=height)
        

        self.frame=0
        #self.image = self.image_list[type]
        self.image =self.image_list[self.frame]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y-(height*2)
        
        self.estado=estado
        self.naturaleza= naturaleza

        self.animation=self.image_list
        self.frame_rate_ms=frame_rate_ms
        
        self.tiempo_transcurrido_animation=0

        self.colision_rect=pygame.Rect(self.rect)
        self.colision_rect.width=self.rect.width/4
        self.colision_rect.x = self.rect.x +(self.rect.width/2)
        

    def draw(self,screen):
        self.image =self.image_list[self.frame]
        #if self.estado :
        screen.blit(self.image,self.rect)
        #if(DEBUG):
           # pygame.draw.rect(screen,color=C_RED,rect=self.collition_rect)
         #   pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
          
          #  pygame.draw.rect(screen,color =(255,100,255),rect=self.terreno_colision_rect)
    #def update(self)

    '''
    def asignar_imagen(self,path,cant_fotogramas,width,height):
        if self.tipo_imagen == "muchas":
            lista_imagenes = 
            
        elif(self.tipo_imagen=="sprite"):
            lista_imagenes = Auxiliar.getSurfaceFromSpriteSheet(path,7,9,scale=1)
        return lista_imagenes
    '''

    def update(self,delta_ms):
        self.do_animation(delta_ms)
    

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation)-1 ):
                self.frame += 1 
                print(self.frame)
            else: 
                self.frame = 0
            
    