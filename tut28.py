#Chelin Tutorials. Todos los Derechos Reservados.
#sitio web: http://chelintutorials.blogspot.com/


import pygame
import random


class Recs(object):
    def __init__(self,numeroinicial):
        self.lista=[]
        for x in range(numeroinicial):
            #creo un rect random
            leftrandom=random.randrange(2,560)
            toprandom=random.randrange(-580,-10)
            width=random.randrange(10,30)
            height=random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))            
    def reagrear(self):
        for x in range(len(self.lista)):
            if self.lista[x].top>482:
                leftrandom=random.randrange(2,560)
                toprandom=random.randrange(-580,-10)
                width=random.randrange(10,30)
                height=random.randrange(15,30)
                self.lista[x]=(pygame.Rect(leftrandom,toprandom,width,height)) 

    def agregarotro(self):
        pass
    def mover(self):
        for rectangulo in self.lista:
            rectangulo.move_ip(0,2)
    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(200,0,0),rectangulo)
            
class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen

        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False
            

def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((600,480))
    salir=False
    reloj1= pygame.time.Clock()
    imagen1=pygame.image.load("nave.png").convert_alpha()
    imagenexplosion=pygame.image.load("explosion.png").convert_alpha()
    imagenfondo=pygame.image.load("fondo.png").convert_alpha()
    
    recs1=Recs(25)
    player1=Player(imagen1)
    
    #variables aux
    player1=Player(imagen1)
    vx,vy=0,0
    velocidad=10
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    colisiono=False
    
    
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if colisiono==False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=True
                        vx=-velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=True
                        vx=velocidad
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy=-velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=True
                        vy=velocidad
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=velocidad
                        else:vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-velocidad
                        else:vx=0
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=velocidad
                        else:vy=-0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-velocidad
                        else:vy=0                    
        
        reloj1.tick(20)
        

        if colision(player1,recs1):
            colisiono=True
            player1.imagen=imagenexplosion
        if colisiono==False:    
            recs1.mover()
            player1.mover(vx, vy)     
               
        pantalla.blit(imagenfondo,(0,0))
        recs1.pintar(pantalla)
        player1.update(pantalla)
        pygame.display.update()
        recs1.reagrear()        
    pygame.quit()

main()