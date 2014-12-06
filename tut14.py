import pygame
import random
def main():
    pygame.init()
    sonido1=pygame.mixer.Sound("thud.wav")
    pantalla=pygame.display.set_mode((480,500))
    fuente1= pygame.font.SysFont("Arial", 25, True, False)
    info0=fuente1.render("Presione el mouse para empezar..",0,(255,255,255))
    info=fuente1.render("Tenes 10 segudos",0,(255,255,255))
    info2=fuente1.render("Espacio para volver a jugar",0,(255,255,255))
    salir=False
 
    listarec=[]

    termino=False
    empezo=False
    r1= pygame.Rect(0,0,10,10)
    rotos=0
    reloj1= pygame.time.Clock()
    segundosint=0
    for x in range(50):
        w= random.randrange(5,25)
        h= random.randrange(5,25)
        x= random.randrange(470)
        y=random.randrange(490)
        listarec.append(pygame.Rect(x,y,w,h))
    if empezo==False:
        while empezo==False:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print "Done"
                    empezo="True"
            pantalla.blit(info0,(50,100))
            pygame.display.update()
    segini=pygame.time.get_ticks()/1000
    while salir!=True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                salir=True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for recs in listarec:
                    if termino==False :
                       if r1.colliderect(recs):
                            sonido1.play()
                            recs.width=0
                            recs.height=0
                            recs.top=-100
                            recs.left=-100
                            rotos+=1
            if event.type ==pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    pygame.quit()
                    return 1
            
        reloj1.tick(20)
        (r1.left,r1.top)=pygame.mouse.get_pos()
        r1.left-=r1.width/2
        r1.top-=r1.height/2
        
        pantalla.fill((0,0,0))
        for recs in listarec:
            pygame.draw.rect(pantalla,(0,200,0),recs)
        pygame.draw.rect(pantalla,(200,20,20),r1)   
        pantalla.blit(info,(5,5))
        if segundosint>=10:
            termino=True
        if termino==False:
            segundosint= pygame.time.get_ticks()/1000 -segini
            segundos= str(segundosint)
            contador=fuente1.render(segundos,0,(155,155,255))
        else:
            contador=fuente1.render(segundos+" Usted rompio: "+str(rotos),0,(155,155,255))
            pantalla.blit(info2,(100,200))
        pantalla.blit(contador,(250,5))
        
        pygame.display.update()
        
    pygame.quit()
    return 0
    
if main()==0:
    print "closed"
else:
    print "RE"
    main()
   