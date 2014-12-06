# Chelin Tutorials Todos los Derechos Reservados
# www.chelintutorials.blogspot.com
#Como cambiar el fondo con botones

import pygame 
 # importo el modulo

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
         

#funcion main
def main():
    pygame.init() # inicializo el modulo
    
    # fijo las dimensiones de la pantalla a 300,300 y creo una superficie que va ser la principal
    pantalla=pygame.display.set_mode((500,400))
    
    pygame.display.set_caption("Cambia Colores by Chelin") # Titulo de la Ventana
    #creo un reloj para controlar los fps
    reloj1=pygame.time.Clock()
    
    rojo1=pygame.image.load("rojo.png")
    rojo2=pygame.image.load("rojo2.png")
    azul1=pygame.image.load("azul.png")
    azul2=pygame.image.load("azul2.png")    
    
    boton1=Boton(rojo1,rojo2,200,100)
    boton2=Boton(azul1,azul2,200,200)
    cursor1=Cursor()
    
    blanco=(255,255,255) # color blanco en RGB
    rojo=(200,0,0)
    azul=(0,0,200)
    colordefondo=blanco
    
    
    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        #recorro todos los eventos producidos
        #en realidad es una lista
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    colordefondo=rojo
                if cursor1.colliderect(boton2.rect):
                    colordefondo=azul
            
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir=True
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        pantalla.fill(colordefondo) # pinto la superficie de blanco        
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla, cursor1)

        
        pygame.display.update() #actualizo el display
        
    pygame.quit()
    
main() 