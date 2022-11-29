import pygame
from auxiliar import Auxiliar
from constantes import *

class Bullet:
    def __init__(self,x,y,direction,direccion_de_bala,estado_de_bala,speed=10,angulo_y_de_disparo=0) :
        self.image_sprite_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"extras/enemies_extras/bullet/tile{0}.png",2,flip=False)
        self.image_sprite_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"extras/enemies_extras/bullet/tile{0}.png",2,flip=True)
        self.frame=0
        self.animation=self.image_sprite_l
        self.image=self.animation[self.frame]
        self.rect=self.image.get_rect()
        self.speed_bullet=speed
        self.rect.x=x
        self.rect.y=y
        self.direction=direction
        #self.lista_balas=[]
        #self.disparo=0
        self.angulo_y_de_disparo=angulo_y_de_disparo
        self.direccion_de_bala=direccion_de_bala
        self.terreno_colision_rect=pygame.Rect(self.rect)
        self.terreno_colision_rect.x=self.rect.x
        self.terreno_colision_rect.y=self.rect.y
        self.estado_de_bala=estado_de_bala
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms=100
   
    def draw(self,screen):
        self.image =self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if DEBUG:
            pygame.draw.rect(screen,color=C_PINK,rect=self.terreno_colision_rect)
        

    

            
            

            
        


    #def mov_y(self):
    def do_movement(self,delta_ms):
        if self.direction== DIRECTION_R :
            self.animation=self.image_sprite_r
            self.rect.x += self.speed_bullet
            
            self.rect.y += self.angulo_y_de_disparo

           
        elif(self.direction == DIRECTION_L ):
            self.animation=self.image_sprite_l
            self.rect.x = self.rect.x - self.speed_bullet

        self.terreno_colision_rect.x=self.rect.x
        self.terreno_colision_rect.y=self.rect.y


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

    def update(self,delta_ms):
       
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        
    
    '''
    def agregar_disparo(self,x,y,direction):
        
        self.lista_balas.append(Bala(x,y,direction))

    '''	
    

