from numpy import sin,cos,pi
import pygame as pg
import os
from constants import *



# Size
size = (1300,760)
origin = (750,150)





def inputk1_():
    return 0

def inputk2_():
    return 0

def f2nonlinear_linear(theta,phi):     # we defined second auxillary equation from nonlinear term.
    return -((gammal)*phi)-(w0*sin(theta))

def f2linear_linear(theta,phi):     # we defined second auxillary equation from nonlinear term.
    return -((gammal)*phi)-(w0*theta)


def load_image(image, scale=1):
    fullname = os.path.join("./imgs/", image)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)
    image = image.convert()
    
    return image
    

class Pendulum():
    """

    """
    def __init__(self,length,theta,phi,K2,image,origin,color=(0,0,0),ball_radius = 10,fps=60):
        self.length = length
        self.theta = theta
        self.phi = phi
        self.h = 1/fps
        self.K2 = K2
        self.image = image
        self.color = color
        self.origin = origin
        self.ball_radius = ball_radius
        self.image = load_image(image)

        
    def update(self):
        """
        this is function which work with initial conditions. uses Runge kutta method at it's core.
        """
        k1 = self.h*self.phi
        l1 = self.h*self.K2(self.theta,self.phi)
        k2 = self.h*(self.phi+(l1*0.5))
        l2 = self.h*self.K2(self.theta+(k1*0.5),self.phi+(l1*0.5))
        k3 = self.h*(self.phi+(l2*0.5))
        l3 = self.h*(self.K2(self.theta+(k2*0.5),self.phi+(l2*0.5)))
        k4 = self.h*(self.phi+l3)
        l4 = self.h*(self.K2(self.theta+k3,self.phi+l3))
        k_ = (1/6)*(k1+k4+2*(k2+k3))
        l_ = (1/6)*(l1+l4+2*(l2+l3))
        self.theta+=k_
        self.phi+=l_
    
        
    def draw(self,screen):
        """
        simple pygame drawing methods.
        """
        x=self.origin[0]+(self.length*cos((pi*1.5)-self.theta))
        y=self.origin[1]-(self.length*sin((pi*1.5)-self.theta))
        pg.draw.aaline(screen,self.color,start_pos=self.origin,end_pos=(x+self.ball_radius,y+self.ball_radius))
        screen.blit(self.image,(x,y)) # better try something like drawing a circle


class Simulation:
    """

    """
    def __init__(self,bg,size):
        pg.init()
        self.window = pg.display.set_mode(size, pg.NOFRAME)
        self.bg = bg
        
    def run(self):
        run = True
        clock = pg.time.Clock()
        pendulum1 = Pendulum(length=l,theta=theta_initial,phi=phi_initial, K2=f2nonlinear_linear,image="bitmap1.png",origin=origin,fps=120)
        pendulum2 = Pendulum(length=l,theta=theta_initial,phi=phi_initial, K2=f2linear_linear,image="bitmap2.png",origin=origin,fps=120)
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
            clock.tick(fps)
            self.window.fill(self.bg)
            # draw pendulumswith class
            pendulum1.draw(self.window)
            pendulum2.draw(self.window)

        


        
            # update pendulums
            pendulum1.update()
            pendulum2.update()
            pg.display.update()
        pg.quit()


class Menu:
    """

    """
    def __init__(self,bg,size):
        pg.init()
        self.window = pg.display.set_mode(size, pg.NOFRAME)
        self.bg = bg
        
    def run(self):
        run = True
        clock = pg.time.Clock()
        pendulum1 = Pendulum(length=l,theta=theta_initial,phi=phi_initial, K2=f2nonlinear_linear,image="bitmap1.png",origin=origin,fps=120)
        pendulum2 = Pendulum(length=l,theta=theta_initial,phi=phi_initial, K2=f2linear_linear,image="bitmap2.png",origin=origin,fps=120)
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
            clock.tick(fps)
            self.window.fill(self.bg)
            pendulum1.draw(self.window)
            pendulum2.draw(self.window)
            
        


            pendulum1.update()
            pendulum2.update()
            pg.display.update()
        pg.quit()

class Demo:
    """

    """
    def __init__(self,bg,size):
        pg.init()
        self.window = pg.display.set_mode(size, pg.NOFRAME)
        self.bg = bg
        
    def run(self):
        run = True
        clock = pg.time.Clock()
        pendulum1 = Pendulum(length=l,theta=theta_initial,phi=phi_initial, K2=f2nonlinear_linear,image="bitmap1.png",origin=origin,fps=120)
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
            clock.tick(fps)
            self.window.fill(self.bg)

        


        
            pg.display.update()
        pg.quit()




if __name__=="__main__":
    k = Simulation("#ffffff",size=size)
    k.run()
