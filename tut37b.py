# Chelin Tutorials 2011 Todos los Derechos Reservados.
# www.chelintutorials.blogspot.com

import pygame 
 # importo el modulo

class Target():
    """Clase del objetivo debo cambiar la implementacion para que la imagen se pinte en distinto lugar que el rect"""
    def __init__(self):
        self.x=70
        self.y=70
        
        self.imagen=pygame.image.load("tut37ninja.png") 
        self.rect=self.imagen.get_rect()
        
        self.rect.inflate_ip(-70,-70) #reduzco el rectangulo
        self.rect.topleft=(100,100)   #lo pongo donde quiero
                   
    def pintar(self,pantalla,pintar_rect):
        """Funcion para pintar en la pantalla"""
        pantalla.blit(self.imagen,(self.x,self.y))
        
        if pintar_rect:
            pygame.draw.rect(pantalla,(255,0,0),self.rect)
        
class Cursor():
    """Clase del cursor, mira"""
    def __init__(self,x,y):
        self.imagen=pygame.image.load("tut37mira.png")
        self.rect=pygame.Rect((x-15,y-15),(5,5))
 
    
    def pintar(self,pantalla,x,y):
        """funcion para pintar el cursor en la posicion x,y que recibe por parametro"""
        #cambio el lugar del rectangulo del cursor
        self.rect.topleft=(x+5,y+5)
        
        pantalla.blit(self.imagen,(x-15,y-15))
        pygame.draw.rect(pantalla,(255,0,0),self.rect)


def main():
    """Funcion principal"""
    pygame.init()
    
    pantalla=pygame.display.set_mode((400,400))
    reloj1=pygame.time.Clock()
    sonido1=pygame.mixer.Sound("tut37disparar.wav")
    sonido2=pygame.mixer.Sound("tut37hited.wav")
    
    x,y=pygame.mouse.get_pos()
    #creo el target y el cursor
    target1=Target()
    cursor1=Cursor(x,y)   
     
    blanco=(255,255,255) # color blanco en RGB

    salir=False
    
    #LOOP PRINCIPAL
    while salir!=True:
        reloj1.tick(15)
        pintar_rect=False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
        
            if event.type ==pygame.MOUSEBUTTONDOWN:
                sonido1.play()
                
                if cursor1.rect.colliderect(target1.rect):
                    pintar_rect=True
                    sonido2.play()
        
        
        pantalla.fill(blanco)
        
        #pinto el target
        target1.pintar(pantalla,pintar_rect)
        
        #pinto el cursor
        x,y=pygame.mouse.get_pos()
        cursor1.pintar(pantalla,x,y)
        
        pygame.display.update() 
        
    pygame.quit()
    
main() 