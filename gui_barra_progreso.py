import pygame
from constantes import *
from gui_widget import Widget, Boton,Punto
from auxiliar import Auxiliar


class Barra_progresiva():
    def __init__(self, master_surface, x, y, w, h, color_background,path_imagen_barra,estilo_barra, path_imagen_punto,estilo_punto,p_scale,valor_a_dibujar,valor_max,estado):
        self.master_surface=master_surface
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color_background=color_background

        self.list_image_barra=Auxiliar.getSurfaceFromSeparateFiles(path_imagen_barra,estilo_barra,flip=False,scale=p_scale,w=w,h=h)

        self.image=self.list_image_barra[0]
       # self.lista_valores=lista_valores

       # self.valor_max=len(lista_valores)
        self.valor_a_dibujar=valor_a_dibujar
        self.valor_max=valor_max
        self.ancho_total=int(w)
        self.ancho_imagen_punto=int(w/self.valor_max)
        self.lista_image_punto=Auxiliar.getSurfaceFromSeparateFiles(path_imagen_punto,estilo_punto,flip=False,scale=p_scale,w=self.ancho_imagen_punto,h=h,repeat_frame=5)
        self.image_punto=self.lista_image_punto[0]
        self.path_imagen_punto=path_imagen_punto
       # self.image_punto.width=self.image.width/self.valor_max
        self.image_punto_rect=self.image_punto.get_rect()
        
        self.lista_puntos=[]
        self.lista_puntos=self.generar_coordenadas()

        self.surface=self.image
        self.rectangulo=self.surface.get_rect()
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y
        self.estado=estado

     #   self.lista_puntos_a_imprimir=[]


    def render(self):
        self.surface=self.image
        #print(self.lista_image_punto)
       
            

    def do_increment(self,valor):
        contador_puntos=0
        for punto in self.lista_puntos:
            if contador_puntos<=valor-1:
                punto.estado=1
            #    punto.draw()
            else:
                punto.estado=0

               
            contador_puntos+=1    
           # print("Vida={0} estado_de_instancia_vida={1}".format(contador_puntos,punto.estado))

    def update(self,valor):

        self.render()    
        self.do_increment(valor)
        
       # self.lista_puntos=self.generar_coordenadas()
    #    self.actualizar_puntos()

  #  def actualizar_puntos(self):
   #     for punto in self.lista_puntos:
   #         if punto.estado==1:
    #            self.lista_puntos_a_imprimir.append(punto)    

    def draw(self):
        
     #   super().draw
        
        
        self.master_surface.blit(self.surface,self.rectangulo)
        for punto in self.lista_puntos:
         
            if punto.estado==1:
                punto.rectangulo.x=punto.x+self.rectangulo.x
                punto.rectangulo.y=punto.y+self.rectangulo.y
                self.master_surface.blit(punto.surface,punto.rectangulo)
              #  self.master_surface.blit(self.surface,self.rectangulo)
              #  print("PUNTOS_ESTADO_1".format(punto.estado))
           #     print("IMpreSION DE VIDAS: rect.x={0}  vida.estado={1}".format(punto.x,punto.estado))
       

    def generar_coordenadas(self):
        lista_puntos=[]
      #  print("ANCHO_IMAGE:{0}".format(self.ancho_imagen_punto))
     #   print(self.valor_max)
     #   print("VALOR_PROGRESIVO: {0}".format(self.valor_a_dibujar))
       # dic_image={}
        #contador_i=0
        for i in range (0,self.ancho_total-self.ancho_imagen_punto,self.ancho_imagen_punto):
           # imagen=self.image_punto
            lista_puntos.append(Punto(master_surface=self.image,x=i,y=0,w=self.ancho_imagen_punto,h=self.image_punto_rect.height,color_background=C_BLUE_2,estado=0,imagen_background=self.image_punto))
           
        return lista_puntos