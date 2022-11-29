import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemigo_corredor:
    def __init__(self,x,y,path,cant_fotogramas,speed_walk,frame_rate_ms,move_rate_ms,p_scale=1):
        
        self.walk_l_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=False,scale=p_scale)
        self.walk_r_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=True,scale=p_scale)
        self.frame=0
        self.animation=self.walk_r_list
        self.image=self.animation[self.frame]
        
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.frame_rate_ms=frame_rate_ms
        self.speed_walk=speed_walk
        self.move_rate_ms=move_rate_ms
        self.direction=DIRECTION_R
        self.tiempo_transcurrido_animation=0

        self.terreno_colision_rect=self.image.get_rect()
        self.terreno_colision_rect.x=x
        self.terreno_colision_rect.y=y
        self.terreno_colision_izquierda_rect=pygame.Rect(self.rect.x,y,5,self.rect.height)
        self.terreno_colision_derecha_rect=pygame.Rect(self.rect.x+self.rect.width,y,5,self.rect.height)
       # self.terreno_colision_izquierda_rect.x=self.rect.x+(self.rect.width)
        self.colision_superior_damage_rect=pygame.Rect(x,y,(self.rect.width/1.5),self.rect.height)

        self.colision_superior_damage_rect.x=self.rect.x
        self.colision_superior_damage_rect.height=15


        self.estado=1

    def draw(self,screen):
        self.image =self.animation[self.frame]
        
        screen.blit(self.image,self.rect)  

        if DEBUG:
            pygame.draw.rect(screen,color=C_VIOLET,rect=self.terreno_colision_izquierda_rect)
         #   pygame.draw.rect(screen,color=(128,128,0),rect=self.terreno_colision_derecha_rect)
            pygame.draw.rect(screen,color=C_LIGHT_PINK,rect=self.terreno_colision_derecha_rect)
            pygame.draw.rect(screen,color=C_YELLOW_GREEN,rect=self.colision_superior_damage_rect)

    def do_movement(self,delta_ms):
        if self.direction == DIRECTION_R :
            self.animation=self.walk_r_list
            self.rect.x+=self.speed_walk
           # self.terreno_colision_rect.x+=self.speed_fly
            self.terreno_colision_izquierda_rect.x+=self.speed_walk
            self.terreno_colision_derecha_rect.x+=self.speed_walk
            self.colision_superior_damage_rect.x+=self.speed_walk


        else :
            self.animation=self.walk_l_list
            self.rect.x+= -self.speed_walk
          #  self.terreno_colision_rect.x+=-self.speed_fly
            self.terreno_colision_izquierda_rect.x+= -self.speed_walk
            self.terreno_colision_derecha_rect.x+= -self.speed_walk
            self.colision_superior_damage_rect.x+= -self.speed_walk


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

