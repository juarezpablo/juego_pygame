import pygame
from constantes import *
from player import Player
from plataforma import Plataform
from enemy import Enemigo
from recompensas import Botin

from enemigo_tipo_volador import Enemigo_volador
from enemigo_estatico import Enemigo_estatico
from proyectil import Bala
from proyectil_enemigo import Bullet

from enemigo_corredor import Enemigo_corredor

from gui_barra_progreso import Barra_progresiva

from portal import Portal_meta

import json
import re

from formularios import Form


'''
"stage_1":{
    "plataformas":
        [
            {  "x": 450 ,"y":500 ,"widht": 50, "height":50,"type":2},
            { "x": 450 ,"y":500 ,"widht": 50, "height":50,"type":2}
        ],
    "enemigos":
        {
        "volador": [{},{}]
        "estaticos": [{},{}]  
        }  {"x": 1300,"y": 600, "clase": "dog_bone","speed_walk":3,"frame_rate_ms":80, "move_rate_ms":30,"p_scale":1}
    }
'''


                    
#clases_de_portales=[{"clase":"portal_1", "path": PATH_IMAGE+"extras/elements/portal/portal-stay/tile{0}.png", "cant_fotogramas":15},]



class Nivel():
    def __init__(self,cantidad_enemigos,path,cant_plataformas=10,key_stage=2,master_surface=1,active=False):

        self.datos_json=self.cargar_json(path)
        self.datos_clases=self.datos_json["clases"]
        self.datos_enemigos=self.datos_json["enemigos"]
        self.lista_plataformas=[]
        self.cantidad_enemigos=cantidad_enemigos
        self.cantidad_plataformas=cant_plataformas
        self.lista_plataformas=self.crear_plataformas()

        self.lista_enemigos=[]
        #self.lista_enemigos=self.crear_enemigos()
        self.imagen_fondo = pygame.image.load(PATH_IMAGE+"locations/set_bg_05/3_game_background/3_game_background.png").convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.rect=self.imagen_fondo.get_rect()

        self.lista_botines=[]
        self.lista_botines=self.crear_botines()

        self.lista_enemigos_voladores=[]
        self.lista_enemigos_voladores=self.crear_enemigos_voladores()
        self.lista_enemigos_estaticos=[]
        self.lista_enemigos_estaticos=self.crear_enemigos_estaticos()

        self.lista_enemigos_corredores=[]
        self.lista_enemigos_corredores=self.crear_enemigos_corredores()
        self.lista_portales=[]
        self.lista_portales=self.crear_portales()

        self.municion_enemiga=[]
        self.tiempo_recarga_enemigos=0
        self.tiempo_desde_colision=0

        self.bandera=0

        self.tiempo_desde_colision_con_daño=0
        self.tiempo_dañado=2000
        self.bandera_daño=0
       # self.player_vidas=2
        #self.player_barra_vida=Barra_progresiva(self.imagen_fondo,1200,50,200,25,C_LIGHT_PINK,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Background0{0}.png",1,PATH_IMAGE+"gui/set_gui_01/Pixel_Border/Bars/Bar_Segment0{0}.png",estilo_punto=1,p_scale=1,valor_a_dibujar=3,valor_max=6,estado="s")

    def cargar_json(self,path):
        diccionario={}
        with open(path,"r",encoding="utf8") as archivo:
            diccionario = json.load(archivo)
            #print(diccionario)
            return diccionario

    def crear_portales(self):
        for portal in self.datos_json["portales_a_procesar"]:
            for elemento in self.datos_clases["clases_de_portales"]:
                if portal["clase"]==elemento["clase"]:
                    self.lista_portales.append(Portal_meta(x=portal["x"],y=portal["y"],path=PATH_IMAGE+elemento["path"],cant_fotogramas=elemento["cant_fotogramas"],frame_rate_ms=portal["frame_rate_ms"],move_rate_ms=portal["move_rate_ms"],direction=portal["direction"],p_scale=portal["p_scale"]))

        return self.lista_portales

    def crear_plataformas(self): 
        for item_plataforma in self.datos_json["plataformas_a_procesar"] :
            for elemento in self.datos_clases["clases_de_plataformas"]:
                if item_plataforma["clase"] == elemento["clase"] :
                    self.lista_plataformas.append(Plataform(x=item_plataforma["x"],y=item_plataforma["y"],width=item_plataforma["widht"],height=item_plataforma["height"],type=item_plataforma["type"], path=PATH_IMAGE+elemento["path"],cant_fotogramas =elemento["cant_fotogramas"], naturaleza=item_plataforma["naturaleza"]))
        return self.lista_plataformas    


   # def crear_enemigos(self):
       # for item in enemigos_a_procesar:
       #     self.lista_enemigos.append(Enemigo(x=item["x"],y=item["y"],speed_walk=item["speed_walk"],speed_run=item["speed_walk"],gravity=item["gravity"],jump_power=item["jump_power"],frame_rate_ms=item["frame_rate_ms"],move_rate_ms=item["move_rate_ms"],jump_height=item["jump_height"],p_scale=item["p_scale"],interval_time_jump=item["interval_time_jump"]))
       # return self.lista_enemigos    

    def update(self,delta_ms,player_municion_list,player_1):

       # self.player_vidas=player_1.vidas
        self.colisiones(player_municion_list,player_1,delta_ms)   
        contador_index=0
        contador_index_botin=0
        contador_index_municion_enemiga=0
        contador_index_bala=0

        contador_index_enemigo_estatico=0
        contador_index_enemigo_corredor=0

        for enemigo in self.lista_enemigos:
            enemigo.automatize(delta_ms)
            enemigo.update(delta_ms,self.lista_plataformas,player_municion_list)  
            if enemigo.estado==False:
                self.lista_enemigos.pop(contador_index)
            contador_index+=1
        for botin in self.lista_botines:
            if botin.estado==0 :
                self.lista_botines.pop(contador_index_botin)
            contador_index_botin+=1
            botin.update(delta_ms)
        
        for bala in player_municion_list:
            if bala.estado_de_bala =="colision_terreno" :
                player_municion_list.pop(contador_index_bala)
            contador_index_bala+=1    
            bala.update()

        for enemigo_volador in self.lista_enemigos_voladores:
            enemigo_volador.update(delta_ms)

        for enemigo_estatico in self.lista_enemigos_estaticos:
            if enemigo_estatico.estado==0:
                self.lista_enemigos_estaticos.pop(contador_index_enemigo_estatico)
            contador_index_enemigo_estatico+=1    
            enemigo_estatico.update(delta_ms)

        for municion_enemiga in self.municion_enemiga:
            if municion_enemiga.estado_de_bala =="colision_terreno" :
                self.municion_enemiga.pop(contador_index_municion_enemiga)
            contador_index_municion_enemiga+=1  
            municion_enemiga.update(delta_ms)

        for enemigo_corredor in self.lista_enemigos_corredores:
            if enemigo_corredor.estado==0:
                self.lista_enemigos_corredores.pop(contador_index_enemigo_corredor)
            contador_index_enemigo_corredor+=1    
            enemigo_corredor.update(delta_ms)

        #self.player_barra_vida.update(self.player_vidas)
        for portal in self.lista_portales:
            portal.update(delta_ms)
                
    def colisiones(self,player_municion_list,player_1,delta_ms):

        for bala in player_municion_list:
            for plataforma in self.lista_plataformas:
                if bala.terreno_colision_rect.colliderect(plataforma.terreno_colision_rect):
                    bala.estado_de_bala="colision_terreno"

        for enemigo_volador in self.lista_enemigos_voladores:
            for plataforma in self.lista_plataformas:
                if enemigo_volador.terreno_colision_derecha_rect.colliderect(plataforma.terreno_colision_rect)  and plataforma.naturaleza =="solida" :
                    if enemigo_volador.direction==DIRECTION_R:
                        enemigo_volador.direction=DIRECTION_L
                if enemigo_volador.terreno_colision_izquierda_rect.colliderect(plataforma.terreno_colision_rect) and plataforma.naturaleza =="solida" :
                    if enemigo_volador.direction == DIRECTION_L:
                        enemigo_volador.direction=DIRECTION_R

        for enemigo_corredor in self.lista_enemigos_corredores:
            for plataforma in self.lista_plataformas:
                if enemigo_corredor.terreno_colision_derecha_rect.colliderect(plataforma.terreno_colision_rect)  and plataforma.naturaleza =="solida" :
                    if enemigo_corredor.direction==DIRECTION_R:
                        enemigo_corredor.direction=DIRECTION_L
                if enemigo_corredor.terreno_colision_izquierda_rect.colliderect(plataforma.terreno_colision_rect) and plataforma.naturaleza =="solida" :
                    if enemigo_corredor.direction == DIRECTION_L:
                        enemigo_corredor.direction=DIRECTION_R




            if enemigo_corredor.colision_superior_damage_rect.colliderect(player_1.ground_collition_rect):
                enemigo_corredor.estado=0   

            if enemigo_corredor.terreno_colision_derecha_rect.colliderect(player_1.collition_rect) or enemigo_corredor.terreno_colision_izquierda_rect.colliderect(player_1.collition_rect):
                player_1.estado_player="herido"
                self.descontar_vida_player(delta_ms,player_1) 





        for enemigo_estatico in self.lista_enemigos_estaticos:
            for bala in player_municion_list:
                if bala.terreno_colision_rect.colliderect(enemigo_estatico.rect):
                    enemigo_estatico.estado=0
                    bala.estado_de_bala="colision_terreno"

        for enemigo_estatico in self.lista_enemigos_estaticos:
            if player_1.collition_rect.colliderect(enemigo_estatico.colision_rango_izquierda_player_rect) and enemigo_estatico.direction==DIRECTION_L:
                
                self.crear_bala(enemigo_estatico.rect.x,(enemigo_estatico.rect.y+(enemigo_estatico.rect.height/3)),enemigo_estatico.direction,delta_ms)
                #print(enemigo_estatico.rect.x)
                enemigo_estatico.shoot(on_off = True)
            else:
                enemigo_estatico.shoot(on_off=False)    
        
        for municion_enemiga in self.municion_enemiga:
            for plataforma in self.lista_plataformas:
                if municion_enemiga.terreno_colision_rect.colliderect(plataforma.terreno_colision_rect):
                    municion_enemiga.estado_de_bala="colision_terreno"
            if municion_enemiga.terreno_colision_rect.colliderect(player_1.collition_rect): 
             #   player_1.vidas=player_1.vidas-1 
                player_1.estado_player="herido"
                self.descontar_vida_player(delta_ms,player_1) 
            #print("VIDAS: {0}".format(player_1.vidas))    
        for botin in self.lista_botines:
            if player_1.collition_rect.colliderect(botin.colision_rect):
                botin.estado=0            


    def descontar_vida_player(self,delta_ms,player_1):
        self.tiempo_dañado=500
        
        self.tiempo_desde_colision_con_daño+=delta_ms
        #print("DELTA_MS {0}".format(self.tiempo_desde_colision))
        if  self.bandera_daño==0 :
            player_1.vidas=player_1.vidas-1
            self.bandera_daño=1
            #self.tiempo_recarga_enemigos=0
           # print("RESTO VIDA- VIDA: {0}".format(player_1.vidas))
            player_1.estado_player="sano"
        if self.tiempo_desde_colision_con_daño>self.tiempo_dañado:
            self.tiempo_desde_colision_con_daño=0
            self.bandera_daño=0


    def crear_botines(self):
        for item_botin in self.datos_json["botines_a_procesar"]:
            for elemento in self.datos_clases["clases_de_botines"]:
                if item_botin["clase"]==elemento["clase"]:
                    self.lista_botines.append(Botin(x=item_botin["x"],y=item_botin["y"],width=item_botin["widht"],height=item_botin["height"],type=item_botin["type"], path=PATH_IMAGE+elemento["path"],cant_fotogramas =elemento["cant_fotogramas"], tipo_imagen=elemento["tipo_imagen"], naturaleza=item_botin["naturaleza"], frame_rate_ms=item_botin["frame_rate_ms"] ))
        return self.lista_botines


    def draw(self,screen,player_municion_list):
        for plataforma in self.lista_plataformas:
            plataforma.draw(screen) 

        for enemigo_corredor in self.lista_enemigos_corredores:
            enemigo_corredor.draw(screen)

        for botin in self.lista_botines:
            botin.draw(screen)


        for enemigo in self.lista_enemigos:
            enemigo.draw(screen)          
        for botin in self.lista_botines:
            botin.draw(screen)

        for bala in player_municion_list:
            bala.draw(screen)

        for enemigo_volador in self.lista_enemigos_voladores:
            enemigo_volador.draw(screen)
        for enemigo_estatico in self.lista_enemigos_estaticos:
            enemigo_estatico.draw(screen)    

        for municion in self.municion_enemiga:
            municion.draw(screen)

        for portal in self.lista_portales:
            portal.draw(screen)


       # self.player_barra_vida.draw()

    def crear_enemigos_voladores(self):
        for enemigo in self.datos_enemigos["enemigos_voladores_a_procesar"]:
            for tipo_clase in self.datos_clases["clases_de_enemigos"]:
                if enemigo["clase"]==tipo_clase["clase"]:
                    self.lista_enemigos_voladores.append(Enemigo_volador(x=enemigo["x"], y=enemigo["y"], path= PATH_IMAGE+tipo_clase["path"], cant_fotogramas= tipo_clase["cant_fotogramas"],speed_fly=enemigo["speed_fly"],frame_rate_ms=enemigo["frame_rate_ms"], move_rate_ms=enemigo["move_rate_ms"], p_scale=enemigo["p_scale"] ))

        return self.lista_enemigos_voladores

    def crear_enemigos_corredores(self):
        for enemigo in self.datos_enemigos["enemigos_corredores_a_procesar"]:
            for tipo_clase in self.datos_clases["clases_de_enemigos"]:
                if enemigo["clase"]==tipo_clase["clase"]:
                    self.lista_enemigos_corredores.append(Enemigo_corredor(x=enemigo["x"], y=enemigo["y"], path=PATH_IMAGE+tipo_clase["path"], cant_fotogramas= tipo_clase["cant_fotogramas"],speed_walk=enemigo["speed_walk"],frame_rate_ms=enemigo["frame_rate_ms"], move_rate_ms=enemigo["move_rate_ms"], p_scale=enemigo["p_scale"] ))

        return self.lista_enemigos_corredores




    def crear_enemigos_estaticos(self):
        for enemigo in self.datos_enemigos["enemigos_estaticos_a_procesar"]:
            for tipo_clase in self.datos_clases["clases_de_enemigos"]:
                if enemigo["clase"]==tipo_clase["clase"]:
                    self.lista_enemigos_estaticos.append(Enemigo_estatico(x=enemigo["x"], y=enemigo["y"], path=PATH_IMAGE+tipo_clase["path"], cant_fotogramas= tipo_clase["cant_fotogramas"],frame_rate_ms=enemigo["frame_rate_ms"], move_rate_ms=enemigo["move_rate_ms"], direction=enemigo["direction"] , p_scale=enemigo["p_scale"]))

        return self.lista_enemigos_estaticos

    def crear_bala(self,x,y,direction,delta_ms):
        self.tiempo_recarga_enemigos=2200
        #print("Tiempo RECARGA ENEMY {0}".format(self.tiempo_recarga_enemigos))
        self.tiempo_desde_colision+=delta_ms
        print("DELTA_MS {0}".format(self.tiempo_desde_colision))

        

        if  self.bandera==0 :
            self.municion_enemiga.append(Bullet(x,y,direction,direction,estado_de_bala="disparada",speed=5,angulo_y_de_disparo=y))
            self.bandera=1
            #self.tiempo_recarga_enemigos=0
            print("AGREGO BALA")
        if self.tiempo_desde_colision>self.tiempo_recarga_enemigos:
            self.tiempo_desde_colision=0
            self.bandera=0

       # print(self.municion_enemiga)





