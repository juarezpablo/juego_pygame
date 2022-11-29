import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemigo_estatico:
    def __init__(self,x,y,path,cant_fotogramas,frame_rate_ms,move_rate_ms,direction,p_scale=1):
        
        self.stay_r_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=True,scale=p_scale)
        self.stay_l_list = Auxiliar.getSurfaceFromSeparateFiles(path,cant_fotogramas,flip=False,scale=p_scale)

        self.shoot_r_list=Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"extras/enemies_extras/centauro/shoot/centauro({0}).png",10,flip=True,scale=p_scale)
        self.shoot_l_list=Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"extras/enemies_extras/centauro/shoot/centauro({0}).png",10,flip=False,scale=p_scale)

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

        self.colision_rango_izquierda_player_rect=pygame.Rect(self.rect.x,y,self.rect.width*4,self.rect.height)
        self.colision_rango_izquierda_player_rect.x= (self.rect.x)-(self.rect.width*5)

        self.estado=1

        self.is_shoot=False



    '''
    def shoot(self):
        if self.direction==DIRECTION_R :
            self.animation=self.shoot_r_list
        elif(self.direction==DIRECTION_L):
            self.animation=self.shoot_r_list
            
    '''
    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True ):
            if(self.animation != self.shoot_r_list and self.animation != self.shoot_l_list):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r_list
                    
                else:
                    self.animation = self.shoot_l_list
    

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
        if self.is_shoot==False and self.animation!=self.stay_r_list and self.animation!= self.stay_l_list :
            self.frame=0

            if self.direction==DIRECTION_R  :
                self.animation=self.stay_r_list
            else:
                self.animation=self.stay_l_list    



    def update(self,delta_ms):
        self.stay(delta_ms)
        self.do_animation(delta_ms)





