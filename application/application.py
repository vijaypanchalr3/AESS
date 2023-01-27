import pygame as pg
from numpy import sin,cos,pi
import os
import sys
from constants import gammal, w0


# Size
size = (1300,760)
origin = (750,150)

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
    Pendulum object with all constants and all necesery functions.
    """
    def __init__(self,length,theta,phi,K2,image,origin,fps=60):
        self.length = length    # length of pendulum
        self.theta = theta      # initial angular displacement
        self.phi = phi          # initial angular vel
        self.h = 1/fps          # ! steps, need to be changed !
        self.K2 = K2            # complimetry function
        self.origin = origin    # origin
        self.image = load_image(image) # images for pendulum

        
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
        pg.draw.aaline(screen,"#000000",start_pos=self.origin,end_pos=(x+10,y+10))
        screen.blit(self.image,(x,y)) # better try something like drawing a circle


class Simulation:
    """
    main loop for simulation
    """
    def __init__(self):
        pg.init()
        size = (1300,760)       # need to give flexibility of all displays
        self.window = pg.display.set_mode(size, pg.RESIZABLE)
        pg.display.set_caption("Pendulum simulation - Menu")
        self.ff = pg.font.Font("Lato",20)
        self.size = self.window.get_size()


        # colors
        self.bg = "#000000"
        self.fg = "#ffffff"
        self.special = "#ffffff"
        
    def menu(self):
        run = True
        clock = pg.time.Clock()
        user_text = '0'

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

                
    def run(self):
        # run = True
        # clock = pg.time.Clock()
        # pendulum1 = Pendulum(length=l,theta=theta_initial,phi=phi_initial, K2=f2nonlinear_linear,image="bitmap1.png",origin=origin,fps=120)
        # pendulum2 = Pendulum(length=l,theta=theta_initial,phi=phi_initial, K2=f2linear_linear,image="bitmap2.png",origin=origin,fps=120)
        # while run:
            # for event in pg.event.get():
                # if event.type == pg.QUIT:
                    # run = False
                    # break
            # clock.tick(fps)
            # self.window.fill(self.bg)
            # # draw pendulumswith class
            # pendulum1.draw(self.window)
            # pendulum2.draw(self.window)




        
            # # update pendulums
            # pendulum1.update()
            # pendulum2.update()
            # pg.display.update()
        # pg.quit()
        pg.quit()




if __name__=="__main__":
    k = Simulation("#ffffff",size=size)
    k.run()
