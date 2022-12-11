import pygame

from auxiliar import Auxiliar
from constantes import *
from proyectil import Bala

from gui_widget import Widget
from gui_barra_progreso import Barra_progresiva
from gui_caja_texto import Caja_texto


class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100,tablero=1) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''

        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER_STAY,10,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER_STAY,10,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER_JUMP,10,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER_JUMP,10,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER_WALK,8,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER_WALK,8,flip=True,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/cowgirl/Shoot ({0}).png",3,flip=False,scale=p_scale,repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/cowgirl/Shoot ({0}).png",3,flip=True,scale=p_scale,repeat_frame=2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/cowgirl/Melee ({0}).png",7,flip=False,scale=p_scale,repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE+"caracters/players/cowgirl/Melee ({0}).png",7,flip=True,scale=p_scale,repeat_frame=1)

        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
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

        #self.municion_r=Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"elements/toy_star_1/toy_star_1.png",15,1,False,1,1)
        #print(self.municion_r)
        #self.municion_rect=pygame.Rect(x+self.rect.width,y+self.rect.height/2,50,25)
        
        self.municion_list=[]
        self.angulo_y_de_disparo=0
        self.direccion_bala=DIRECTION_UP


        self.terreno_colision_izquierda_rect=pygame.Rect(self.rect.x,y+5,5,self.rect.height-5)
        self.terreno_colision_derecha_rect=pygame.Rect(self.rect.x+self.collition_rect.width*2,y+5,5,self.rect.height-5)
        self.terreno_colision_izquierda_rect.x=self.rect.x+(self.collition_rect.width)
       # print(self.rect.width)

       # self.lives=[]
        #self.lives=self.generate_lives(5)
        self.vidas=4    

        self.estado_player="sano"
        self.bandera_daño=0
        self.tiempo_desde_colision=0

        self.barra_de_vida=Barra_progresiva(tablero,1200,50,200,25,C_LIGHT_PINK,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Background0{0}.png",1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Segment0{0}.png",estilo_punto=1,p_scale=1,valor_a_dibujar=self.vidas,valor_max=6,estado=1)

        self.tiempo_de_recarga=2000
        self.tiempo_desde_creacion=0
        self.bandera_recarga=0
        self.score=0
        self.score_label=Caja_texto(tablero,500,0,100,50,None,"SCORE","Verdana",C_BLUE_2,35)
        self.score_value=Caja_texto(tablero,650,0,100,50,None,self.score,"Verdana",C_BLUE_2,35)

        self.tiempo_de_juego=0
        self.label_tiempo=Caja_texto(tablero,720,0,100,50,None,"TIME:","Verdana",C_RED,35)
        self.value_tiempo=Caja_texto(tablero,820,0,100,50,None,self.tiempo_de_juego,"Verdana",C_RED,35)

    
    '''

    def generate_lives(self,cant):
        for i in range (cant):
            self.lives.append("coin")
        return self.lives    
    '''


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
                    
    def shoot(self,on_off = True,delta_ms=1):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                    
                else:
                    self.animation = self.shoot_l 
                if (self.animation!=self.walk_r and self.animation!= self.walk_l):      
                    self.municion(delta_ms)        
    
    def municion(self,delta_ms):
        self.tiempo_de_recarga=10
        #print("Tiempo RECARGA ENEMY {0}".format(self.tiempo_recarga_enemigos))
        self.tiempo_desde_creacion+=delta_ms
        #print("DELTA_MS {0}".format(self.tiempo_desde_colision))

        

        if  self.bandera_recarga==0 :
            self.municion_list.append(Bala(self.rect.x,self.rect.y+(self.rect.height/3),self.direction,self.direccion_bala,estado_de_bala="disparada",speed=10,angulo_y_de_disparo=self.angulo_y_de_disparo))
            self.bandera_recarga=1
            #self.tiempo_recarga_enemigos=0
           
        if self.tiempo_desde_creacion>self.tiempo_de_recarga:
            self.tiempo_desde_creacion=0
            self.bandera_recarga=0

        
       
        
    

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.terreno_colision_izquierda_rect.x += delta_x
        self.terreno_colision_derecha_rect.x += delta_x


    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.terreno_colision_izquierda_rect.y += delta_y
        self.terreno_colision_derecha_rect.y += delta_y



    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            if ( not self.colision_con_terreno(plataform_list)):
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
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect) and plataforma.naturaleza == "pisable"):
                    retorno = True
                    break       
        return retorno    

    def colision_con_terreno(self,plataform_list):
        retorno = False
        for plataforma in plataform_list:
            if (self.terreno_colision_izquierda_rect.colliderect(plataforma.terreno_colision_rect) and plataforma.naturaleza =="solida" and self.direction==0):
                retorno= True               
                break
            elif(self.terreno_colision_derecha_rect.colliderect(plataforma.terreno_colision_rect) and plataforma.naturaleza =="solida" and self.direction==1):
                retorno=True
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
 
    def update(self,delta_ms,plataform_list,tablero_de_gestion):
        if tablero_de_gestion.stage_1.active:
            self.tiempo_de_juego=self.tiempo_de_juego+(delta_ms/1000)
           # self.tiempo_de_juego=self.tiempo_de_juego/1000
            self.tiempo_de_juego=round(self.tiempo_de_juego,2)
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)

        self.barra_de_vida.update(self.vidas)

        print("VIDAS: {0}".format(self.vidas))

        self.score_label.update(delta_ms,"SCORE")
        self.score_value.update(delta_ms,self.score)
        self.value_tiempo.update(delta_ms,self.tiempo_de_juego)
        self.label_tiempo.update(delta_ms,"TIME:")

    def descontar_vida(self,delta_ms):
        self.tiempo_danado=2500
        #print("Tiempo RECARGA ENEMY {0}".format(self.tiempo_recarga_enemigos))
        self.tiempo_desde_colision+=delta_ms
        #print("DELTA_MS {0}".format(self.tiempo_desde_colision))

        

        if  self.bandera_daño==0 :
            self.vidas=self.vidas-1
            self.bandera=1
            #self.tiempo_recarga_enemigos=0
            print("RESTO VIDA")
        if self.tiempo_desde_colision>self.tiempo_danado:
            self.tiempo_desde_colision=0
            self.bandera=0

        
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=(128,0,128),rect=self.terreno_colision_izquierda_rect)
            pygame.draw.rect(screen,color=(128,128,0),rect=self.terreno_colision_derecha_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        '''
        if self.animation== self.shoot_l and self.is_shoot==True:
            self.municion_r_image=self.municion_r[0]
            screen.blit(self.municion_r_image,self.municion_rect)
    	'''
        #if self.animation== self.shoot_l and self.is_shoot==True:
        
        self.barra_de_vida.draw()

        self.score_label.draw()
        self.score_value.draw()
        self.label_tiempo.draw()
        self.value_tiempo.draw()
    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms


        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_a]):
            self.shoot(False,delta_ms)  

        if(not keys[pygame.K_a]):
            self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a]):
            self.shoot(True,delta_ms)   
        
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.knife()   
        
        if (keys[pygame.K_UP] and keys[pygame.K_s] ):
            self.angulo_y_de_disparo=self.angulo_y_de_disparo - 1

        if (keys[pygame.K_s] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
            self.angulo_y_de_disparo=0

        if(keys[pygame.K_DOWN]):
            self.angulo_y_de_disparo=self.angulo_y_de_disparo + 1