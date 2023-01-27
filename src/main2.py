import pygame as pg
from numpy import sin,cos,pi
import os
import sys
from constants import *



def load_image(image, scale=1):
    fullname = os.path.join("./imgs/", image)
    image = pg.image.load(fullname)

    # size = image.get_size()
    # size = (size[0] * scale, size[1] * scale)
    # image = pg.transform.scale(image, size)
    # image = image.convert()
    
    return image
    
class Pendulum:
    def __init__(self,length,theta,phi,color="#000000",image = "bitmap.png"):
        self.length = length
        self.theta = theta
        self.phi = phi
        self.color = color
        self.h = 0.0250
        self.image = load_image(image)
    def Auxilaryfun(self,theta,phi):
        return -(gammal*phi)-(w0*sin(theta))

    def update(self):
        """

        """
        k1 = self.h*self.phi
        l1 = self.h*self.Auxilaryfun(self.theta,self.phi)
        k2 = self.h*(self.phi+(l1*0.5))
        l2 = self.h*self.Auxilaryfun(self.theta+(k1*0.5),self.phi+(l1*0.5))
        k3 = self.h*(self.phi+(l2*0.5))
        l3 = self.h*(self.Auxilaryfun(self.theta+(k2*0.5),self.phi+(l2*0.5)))
        k4 = self.h*(self.phi+l3)
        l4 = self.h*(self.Auxilaryfun(self.theta+k3,self.phi+l3))
        k_ = (1/6)*(k1+k4+2*(k2+k3))
        l_ = (1/6)*(l1+l4+2*(l2+l3))
        self.theta+=k_
        self.phi+=l_

    def draw(self,screen,origin):
        """
        
        """
        x=origin[0]+(self.length*cos((pi*1.5)-self.theta))
        y=origin[1]-(self.length*sin((pi*1.5)-self.theta))
        pg.draw.aaline(screen,self.color,start_pos=origin,end_pos=(x+10,y+10))
        screen.blit(self.image,(x,y))


class PendulumAppro(Pendulum):
    def __init__(self, length, theta, phi, color="#000000"):
        super().__init__(length, theta, phi, color)

    def Auxilaryfun(self, theta, phi):
        return -((gammal)*phi)-(w0*theta)
    


class Simulation:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((1360,720),pg.RESIZABLE)
        # self.ff=pg.font.Font("LAto.ttf",28)

        self.fg = "#000000"
        self.bg = "#C7A68B"
        self.special = "#000000"
        self.length = 500
        self.theta = 3.14
        self.phi = 0

    def menu(self):
        run = True
        clock = pg.time.Clock()
        user_text = '0'

        self.size = self.window.get_size()
        
        heading = self.ff.render("Menu",True,self.fg,self.special)
        heading_size = heading.get_size()
        heading_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-heading_size[0]//2,0,heading_size[0]+20,heading_size[1]+10),border_radius=5)
        self.window.blit(heading,heading_rect)
        # option1 = self.ff.render("")
        
        
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    sys.exit()


                # all the keys and control. 



            # pygame quit 
            pg.quit()





    def run1(self):
        run = True
        clock = pg.time.Clock()
        pen = Pendulum(self.length,self.theta,self.phi,image="bitmap1.png")

        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
            # main loop 
            clock.tick(60)
            self.window.fill(self.bg)
            origin = (self.window.get_size()[0]//2,100)
            pen.draw(self.window,origin)
            pen.update()
            pg.display.flip()
        pg.quit()


    def run2(self):
        run = True
        clock = pg.time.Clock()
        
        pen1 = Pendulum(self.length,self.theta,self.phi,color="#000000")
        pen2 = PendulumAppro(self.length,self.theta,self.phi,color="#333333")


        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
            # main loop 
            clock.tick(60)
            self.window.fill(self.bg)
            origin = (self.window.get_size()[0]//2,100)
            pen1.draw(self.window,origin)
            pen2.draw(self.window,origin)
            pen1.update()
            pen2.update()
            pg.display.flip()
        pg.quit()

            
            
                
k = Simulation()
k.run1()
