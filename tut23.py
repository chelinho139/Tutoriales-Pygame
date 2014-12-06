import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((480,300))
    salir=False
    reloj1= pygame.time.Clock()
    imagen1=pygame.image.load("nave.png").convert_alpha()
    player1=Player(imagen1)
    vx,vy=0,0
    velocidad=10
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
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
        player1.mover(vx, vy)
        pantalla.fill((200,200,200))
        player1.update(pantalla)
        pygame.display.update()
                
    pygame.quit()

main()