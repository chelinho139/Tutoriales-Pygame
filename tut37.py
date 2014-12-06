# Chelin Tutorials 2011 Todos los Derechos Reservados.
# www.chelintutorials.blogspot.com

import pygame 
 # importo el modulo

class Target():
    """Clase del objetivo"""
    
    def __init__(self):
        self.imagen=pygame.image.load("tut37ninja.png") #la imagen
        self.rect=self.imagen.get_rect() #el rectangulo
        self.rect.topleft=(70,70) #muevo el rectangulo a la posicion que quiero
                
                
    def pintar(self,pantalla,pintar_rect):
        """Funcion para pintar en la pantalla"""
        pantalla.blit(self.imagen,self.rect) #pinta la imagen
        
        #si la variable pintar_rect es True entonces pinto el rect
        if pintar_rect: 
            pygame.draw.rect(pantalla,(255,0,0),self.rect) #pinta el rect
        
        
class Cursor():
    """Clase del cursor, mira"""
    def __init__(self,x,y):
        self.imagen=pygame.image.load("tut37mira.png") #su imagen
        self.rect=pygame.Rect((x-15,y-15),(5,5)) #su rect
 
    
    def pintar(self,pantalla,x,y):
        """funcion para pintar el cursor en la posicion x,y que recibe por parametro"""
        #cambio el lugar del rectangulo del cursor
        self.rect.topleft=(x+5,y+5) #acomodo el rect
        
        pantalla.blit(self.imagen,(x-15,y-15))#acomodo la imagen para que este en el centro y la pinto
        pygame.draw.rect(pantalla,(255,0,0),self.rect)#pinto el recto


def main():
    """Funcion principal"""
    pygame.init()
    
    pantalla=pygame.display.set_mode((400,400))
    reloj1=pygame.time.Clock() #creo un reloj para los FPS
    
    #creo 2 sonidos
    sonido1=pygame.mixer.Sound("tut37disparar.wav")
    sonido2=pygame.mixer.Sound("tut37hited.wav")
    
    #Variables Auxiliares
    x,y=pygame.mouse.get_pos() #variables aux
    blanco=(255,255,255) # color blanco en RGG
        
    #creo el target y el cursor
    target1=Target()
    cursor1=Cursor(x,y)   
     


    salir=False
    
    #LOOP PRINCIPAL
    while salir!=True:
        reloj1.tick(15)
        pintar_rect=False
        
        #eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
                
            if event.type ==pygame.MOUSEBUTTONDOWN:
                sonido1.play()
                
                #Analizo la colision
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