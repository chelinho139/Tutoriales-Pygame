import pygame 

def main():
    pygame.init()  
    pantalla=pygame.display.set_mode([500,500])
    salir=False

    reloj1=pygame.time.Clock()
    #colores
    blanco=(255,255,255) 
    rojizo=(200,20,50)
    azulado=(70,70,190)

    r1=pygame.Rect(50,50,45,45)
    r2=pygame.Rect(200,200,100,50)
    #Loop Principal!
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if r1.colliderect(r2):
                    r2.height=0
                    r2.width=0

        reloj1.tick(20) #fijo a 20fps
        pantalla.fill(blanco)
        

        (r1.left,r1.top)=pygame.mouse.get_pos()
        r1.left-= r1.width/2
        r1.top-=r1.height/2


        pygame.draw.rect(pantalla,rojizo,r1)
        pygame.draw.rect(pantalla,azulado,r2)
        pygame.display.update() 
        
    pygame.quit()


main()
