import pygame
from constantes import *
from auxiliar import Auxiliar
from proyectil import Bala
from player import Player


class Enemigo(Player):
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale=1, interval_time_jump=100) -> None:
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale, interval_time_jump)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_IDLE_00{0}.png",6,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_IDLE_00{0}.png",6,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_JUMP_00{0}.png",6,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_JUMP_00{0}.png",6,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_RUN_00{0}.png",6,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_RUN_00{0}.png",6,flip=True,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_ATTACK_00{0}.png",6,flip=False,scale=p_scale,repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_ATTACK_00{0}.png",6,flip=True,scale=p_scale,repeat_frame=2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_HURT_00{0}.png",6,flip=False,scale=p_scale,repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/pirate_02/2_entity_000_HURT_00{0}.png",6,flip=True,scale=p_scale,repeat_frame=1)
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.asa=0
        self.municion_list=[]

        self.damage_collition_rect = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
        self.player_collition_rect= pygame.Rect(self.damage_collition_rect)
        #self.player_collition_rect.rect.x=self.rect.x
        #self.player_collition_rect.rect.y=self.rect.y
        

        self.estado= True
        
        

    
    




    def automatize(self,delta_ms):
        
        self.asa=self.asa+delta_ms   
        #print("tiempo transcurrido: {0} mSeg".format(self.asa))
        '''
        if time >2000 and time <5000:
            self.walk(DIRECTION_R)
        elif time >5000 and time <7000:
            self.walk(DIRECTION_L)
        elif time> 7000:
            self.stay()    
            time=0
        
        
        if self.asa>1000 and self.asa<5000:
            self.walk(DIRECTION_R)
        elif(self.asa>5000 and self.asa<6000):
            self.walk(DIRECTION_L)
           
        elif self.asa >6000 :
            if self.asa>6002 and self.asa <6010:
                self.shoot() 
            self.stay()
            self.asa=0
        '''
        if self.asa>1000 and self.asa<10000:
            self.walk(DIRECTION_L)
        elif(self.rect.x<0):
            self.walk(DIRECTION_R)
        elif(self.rect.x > 800 ):
            self.walk(DIRECTION_L)        
    
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno                 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0


        #el enemigo necesita un metodo para cuando recibe daño, debo recorrer en main la lista enemigos y fijarse si colisiona con el rect de colison del player
    def do_damage(self,player_municion_list):
        for bullet in player_municion_list:
            if (self.collition_rect.colliderect(bullet.rect)):
                print("muerto")
                self.estado=False
                

 
    def update(self,delta_ms,plataform_list,player_municion_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.do_damage(player_municion_list)

    



    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l


    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
           #pygame.draw.rect(screen,color=(150,0,100),rect=self.shoot_collition_rect)
        
        self.image = self.animation[self.frame]

        if self.estado == True:
            screen.blit(self.image,self.rect)

        '''
        if self.animation== self.shoot_l and self.is_shoot==True:
            self.municion_r_image=self.municion_r[0]
            screen.blit(self.municion_r_image,self.municion_rect)
    	'''
        #if self.animation== self.shoot_l and self.is_shoot==True:
        for bala in self.municion_list:
            bala.draw(screen)
            bala.update()



