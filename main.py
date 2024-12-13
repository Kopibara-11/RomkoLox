from pygame import *
from random import*
w=500
h=800

screen=display.set_mode((w,h))

background=transform.scale(image.load('bg123.png'),(w,h))

screen.fill((255, 255, 255))



class Mole():
    def __init__(self,x,y,filename,wight,height):
        self.image=transform.scale(image.load(filename),(wight,height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
class Pit():
    def __init__(self,x,y,filename,wight,height):
        self.image=transform.scale(image.load(filename),(wight,height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

holes=[]

x=50
y=250

for i in range(3):
    for j in range(3):
        hole=Pit(x,y,'hole123.png',100,60)
        holes.append(hole)
        x+=150
    y+=150
    x=50

clock=time.Clock()

rand_hole=holes[randint(0,8)]

rand_x,rand_y=rand_hole.rect.x,rand_hole.rect.y

mole=Mole(rand_x+20,rand_y-35,'mole123.png',70,70)


run=True
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False

  
    
    screen.blit(background,(0,0))

    for h in holes:
        h.draw()

    mole.draw()

    clock.tick(60)
    display.update()