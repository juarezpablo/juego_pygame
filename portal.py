import pygame
from constantes import *
from auxiliar import Auxiliar

class Portal_meta:
    def __init__(self,x,y,path,cant_fotogramas,frame_rate_ms,move_rate_ms,direction,p_scale=1):
        
        self.stay_r_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=True,scale=p_scale)
        self.stay_l_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=False,scale=p_scale)


        self.direction=direction
        self.frame=0
        self.animation=self.stay_l_list[self.frame]
        self.image=self.animation
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.frame_rate_ms=frame_rate_ms
        
        self.move_rate_ms=move_rate_ms
        self.tiempo_transcurrido_animation=0

    
        self.estado=1

   



    

    def draw(self,screen):
        self.image =self.animation[self.frame]
        
        screen.blit(self.image,self.rect)  
        if(DEBUG):
            pygame.draw.rect(screen,color=C_RED,rect=self.colision_rango_izquierda_player_rect)



    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation)-1 ):
                self.frame += 1 
                print(self.frame)
            else: 
                self.frame = 0

    def stay(self,delta_ms):
       

        if self.direction==DIRECTION_R  :
            self.animation=self.stay_r_list
        else:
            self.animation=self.stay_l_list    



    def update(self,delta_ms):
        self.stay(delta_ms)
        self.do_animation(delta_ms)

