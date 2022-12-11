import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemigo_volador:
    def __init__(self,x,y,path,cant_fotogramas,speed_fly,frame_rate_ms,move_rate_ms,p_scale=1):
        
        self.fly_l_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=False,scale=p_scale)
        self.fly_r_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=True,scale=p_scale)
        self.frame=0
        self.animation=self.fly_r_list
        self.image=self.animation[self.frame]
        
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.frame_rate_ms=frame_rate_ms
        self.speed_fly=speed_fly
        self.move_rate_ms=move_rate_ms
        self.direction=DIRECTION_R
        self.tiempo_transcurrido_animation=0

        self.terreno_colision_rect=self.image.get_rect()
        self.terreno_colision_rect.x=x
        self.terreno_colision_rect.y=y
        self.terreno_colision_izquierda_rect=pygame.Rect(self.rect.x,y,5,self.rect.height)
        self.terreno_colision_derecha_rect=pygame.Rect(self.rect.x+self.rect.width,y,5,self.rect.height)
       # self.terreno_colision_izquierda_rect.x=self.rect.x+(self.rect.width)

        self.estado=1


    def draw(self,screen):
        self.image =self.animation[self.frame]
        
        screen.blit(self.image,self.rect)  

        if DEBUG:
            pygame.draw.rect(screen,color=C_VIOLET,rect=self.terreno_colision_izquierda_rect)
         #   pygame.draw.rect(screen,color=(128,128,0),rect=self.terreno_colision_derecha_rect)
            pygame.draw.rect(screen,color=C_LIGHT_PINK,rect=self.terreno_colision_derecha_rect)

    def do_movement(self,delta_ms):
        if self.direction == DIRECTION_R :
            self.animation=self.fly_r_list
            self.rect.x+=self.speed_fly
           # self.terreno_colision_rect.x+=self.speed_fly
            self.terreno_colision_izquierda_rect.x+=self.speed_fly
            self.terreno_colision_derecha_rect.x+=self.speed_fly
        else :
            self.animation=self.fly_l_list
            self.rect.x+= -self.speed_fly
          #  self.terreno_colision_rect.x+=-self.speed_fly
            self.terreno_colision_izquierda_rect.x+= -self.speed_fly
            self.terreno_colision_derecha_rect.x+= -self.speed_fly

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation)-1 ):
                self.frame += 1 
                print(self.frame)
            else: 
                self.frame = 0

    def update(self,delta_ms):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)

