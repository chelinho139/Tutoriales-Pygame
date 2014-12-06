import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
    def mover(self,vx,vy):
       pass
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
    
    
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
                
        reloj1.tick(20)
        pantalla.fill((200,200,200))
        player1.update(pantalla)
        pygame.display.update()
                
    pygame.quit()

main()