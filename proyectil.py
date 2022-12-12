
import pygame
from auxiliar import Auxiliar
from constantes import *

class Bala:
    def __init__(self,x,y,direction,direccion_de_bala,estado_de_bala,speed=10,angulo_y_de_disparo=0) -> None:
        self.image_sprite = Auxiliar.getSurfaceFromSpriteSheet("Sprites/images/images/elements/toy_star_1/toy_star_1.png",15,2,False,1,1)
        self.frame=0
        self.rect=self.image_sprite[self.frame].get_rect()
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

        self.delta_x=x

    def draw(self,screen):
        
        screen.blit(self.image_sprite[self.frame],self.rect)
        if DEBUG:
            pygame.draw.rect(screen,color=C_PINK,rect=self.terreno_colision_rect)
        

    def mov_x_y(self):

        if self.direction== DIRECTION_R :
            self.rect.x += (self.speed_bullet)
            
            self.rect.y += self.angulo_y_de_disparo
            print("Angulo Y disparo{0}".format(self.angulo_y_de_disparo))
            
            

            
        elif(self.direction == DIRECTION_L ):
            self.rect.x = self.rect.x - self.speed_bullet

        self.terreno_colision_rect.x=self.rect.x
        self.terreno_colision_rect.y=self.rect.y


    #def mov_y(self):


    def update(self):
       
        self.mov_x_y()
        
    
    '''
    def agregar_disparo(self,x,y,direction):
        
        self.lista_balas.append(Bala(x,y,direction))

    '''	
    

