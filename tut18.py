import pygame

pygame.init()
pantalla=pygame.display.set_mode((480,300))
salir=False
reloj1= pygame.time.Clock()
imagen1=pygame.image.load("alienr.png").convert_alpha()
(x,y)= (100,100)
vx=0
r1=pygame.Rect(250,70,25,500)
sprite1= pygame.sprite.Sprite()
sprite1.image=imagen1
sprite1.rect=imagen1.get_rect()
sprite1.rect.top=100
sprite1.rect.left=50
while salir!=True:#LOOP PRINCIPAL
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx-=10
            if event.key == pygame.K_RIGHT:
                vx+=10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vx=0
            if event.key == pygame.K_RIGHT:
                vx=0    
    
    
    oldx=sprite1.rect.left
    sprite1.rect.move_ip(vx,0) 
    if sprite1.rect.colliderect(r1):
        sprite1.rect.left=oldx
            
    reloj1.tick(15)
    pantalla.fill((255,255,255))
    pygame.draw.rect(pantalla,(0,0,0),r1)
    pantalla.blit(sprite1.image,sprite1.rect)
    pygame.display.update()
            
pygame.quit()