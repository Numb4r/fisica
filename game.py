import pygame
import math
from const import *
from gui import *

Material1=[1,""]
Material2=[1,""]

def define_materials(material1,material2):
    Material1=[material1["indice_refracao"],material1["nome"]]
    Material2=[material2["indice_refracao"],material2["nome"]]

        
class IncidentRay:
    def __init__(self, angle):
        self.x=width/2
        self.y=0
        self.raylen=700
        if 0<angle:
            self.x=0
            self.y=height/2
        if -180<= angle <=-90:
                self.x = pointofmiddle[0]+math.cos(math.radians(angle)) * self.raylen
                self.y = pointofmiddle[1]+math.sin(math.radians(angle)) * self.raylen
                textsurface = myfont.render('Angulo do raio Incidente/Refletido: %f' %(180-angle-270), False, (0, 0, 0))
                screen.blit(textsurface,(20,390))
    def display(self):
        pygame.draw.line(screen, red, pointofmiddle, (self.x,self.y), 3)



        
class ReflectedRay:
    def __init__(self, angle):
        self.raylen=700
        self.ReflectedRayAngle=180-angle
        self.reflectedintensity = (self.ReflectedRayAngle-270)/90
        self.x=width/2
        self.y=0

        if 270 <= self.ReflectedRayAngle <= 360:
            
            self.x = pointofmiddle[0]+math.cos(math.radians(self.ReflectedRayAngle)) * self.raylen
            self.y = pointofmiddle[1]+math.sin(math.radians(self.ReflectedRayAngle)) * self.raylen  
        if 180 >self.ReflectedRayAngle>=0:
            self.x=width
            self.y=height/2

    def display(self):
        pygame.draw.line(screen, red, pointofmiddle, (self.x,self.y), 3)
        
class RefractedRay:
    def __init__(self,angle):
        self.x=width/2
        self.y=0
        self.raylen=700
        TrueAngle = (180-angle-270)
        refractedangle=-math.degrees(math.asin(math.sin(math.radians(TrueAngle))*Material1[0]/Material2[0]))+90
        
        if 0<angle:
            self.x=0
            self.y=height/2
        if -180<= angle <=-90:
                self.x = pointofmiddle[0]+math.cos(math.radians(refractedangle)) * self.raylen
                self.y = pointofmiddle[1]+math.sin(math.radians(refractedangle)) * self.raylen
                textsurface = myfont.render('Angulo do raio refratado: %f' %((refractedangle-90)*-1), False, (0, 0, 0))
                textsurface2 = myfont.render("Indice de Refracao do "+Material1[1]+ ": "+str(Material1[0]), False, (0, 0, 0))
                textsurface3 = myfont.render("Indice de Refracao do "+Material2[1]+": "+str(Material2[0]), False, (0, 0, 0))
                screen.blit(textsurface,(20,500))
                screen.blit(textsurface2,(20,100))
                screen.blit(textsurface3,(20,300))

    def display(self):
        pygame.draw.line(screen, red, pointofmiddle, (self.x,self.y), 3)


class RefractionSurface:
    def __init__(self):
        surface = pygame.Surface((width, pointofmiddle[0]), pygame.SRCALPHA)
        surface.fill((100, 100, 255, 100)) # You can change the 100 depending on what transparency it is.
        screen.blit(surface, (0, pointofmiddle[1]))
        
root = Tk()
Application(root)
root.mainloop()
print(r)
material1=r[0]
material2=r[1]
Material1=[float(material1["indice_refracao"]),material1["nome"]]
Material2=[float(material2["indice_refracao"]),material2["nome"]]


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont(*font)

background_color = (white)
screen = pygame.display.set_mode((width, height))
pygame.draw.line(screen, green, (width/2,1100), (width/2,0), 3)
pygame.display.set_caption('Light Refraction PyGame Simulation')





screen.fill(background_color)

IncidentRay(0).display()
ReflectedRay(0).display()
RefractionSurface()
pygame.display.flip()

angle=0




text = myfont.render("N", False, (0, 0, 0))
screen.blit(text,(0,0))
text = myfont.render(Material1[1], False, (0, 0, 0))
screen.blit(text,(0,50))
text = myfont.render(Material2[1], False, (0, 0, 0))
screen.blit(text,(0,0))

running = True
while running:

    screen.fill(background_color)
    RefractionSurface()
    pygame.draw.line(screen, green, (width/2,1100), (width/2,0), 3)
    text = myfont.render("N", False, (0, 0, 0))
    screen.blit(text,(width/2+10,0))
    text = myfont.render(Material1[1], False, (0, 0, 0))
    screen.blit(text,(width-70,50))
    text = myfont.render(Material2[1], False, (0, 0, 0))
    screen.blit(text,(width-70,height-50))




    pos=pygame.mouse.get_pos()
    angle = math.atan2(pos[1]-(height/2),pos[0]-(width/2))*180/math.pi
    # print(angle)
    (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
    if pressed1:
            IncidentRay(angle).display()
            ReflectedRay(angle).display()
            RefractedRay(angle).display()
            pygame.display.flip()
            (mouseX, mouseY) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


