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

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Pendulum:
    def __init__(self,length,mass,dampcoef,gravity,theta,phi,color="#000000",image = "bitmap.png"):
        self.length = length
        self.w0 = gravity/length
        self.gamma = (length*dampcoef)/mass
        self.theta = theta
        self.phi = phi
        self.color = color
        self.h = 0.0250
        self.image = load_image(image)
    def Auxilaryfun(self,theta,phi):
        return -(self.gamma*phi)-(self.w0*sin(theta))

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
        pg.draw.aaline(screen,self.color,start_pos=origin,end_pos=(x,y))
        screen.blit(self.image,(x-10,y-10))


class PendulumAppro(Pendulum):
    def __init__(self, length, mass, dampcoef, gravity, theta, phi, image,color="#000000"):
        super().__init__(length, mass, dampcoef, gravity, theta, phi,image=image,color=color)

    def Auxilaryfun(self, theta, phi):
        return -((gammal)*phi)-(w0*theta)
    


class Simulation:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((1360,720),pg.RESIZABLE)
        self.ff=pg.font.Font("Lato-BoldItalic.ttf",28)
        self.ff2=pg.font.Font("Lato-BoldItalic.ttf",32)
        
        self.color1 = 0
        self.color2 = 0
        self.color3 = 0
        self.color4 = 0
        
        self.fg = "#000000"
        self.bg = "#C7A68B"
        self.special = "#dddddd"
        self.length = 500
        self.mass = 100
        self.dampcoef = 10
        self.gravity = 10
        self.theta = 3.14
        self.phi = 0
    def slider(self,x,y,pos):
        cursor = pg.mouse.get_pos()
        clicked_pos = pg.mouse.get_pressed()
        pg.draw.rect(self.window,self.fg,(pos+x-5,y-15,10,30))
        pg.draw.rect(self.window,self.fg,(x,y,200,2))
        if x+200>=cursor[0]>x and y+25>=cursor[1]>=y-25:
            if clicked_pos[0]==1:
                # pg.draw.rect(self.window,self.special,(x_scroll,y,50,50))
                pos = cursor[0]-x

        return pos
    def menu(self):
        run = True
        clock = pg.time.Clock()
        user_text = '0'

        self.size = self.window.get_size()
        heading = self.ff2.render("Menu",True,self.fg,self.special)
        heading_size = heading.get_size()
        heading_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-heading_size[0]//2,50,heading_size[0]+20,heading_size[1]+10),border_radius=5)

        
        


        save = self.ff2.render("save",True,self.fg,self.special)
        save_size = save.get_size()
        save_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2+200-save_size[0]//2,self.size[1]-100,save_size[0]+20,save_size[1]+10),border_radius=5)

        cancel = self.ff2.render("cancel",True,self.fg,self.special)
        cancel_size = cancel.get_size()
        cancel_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-200-cancel_size[0]//2,self.size[1]-100,cancel_size[0]+20,heading_size[1]+10),border_radius=5) 

        length = self.length
        mass = self.mass
        dampcoef = self.dampcoef
        gravity = self.gravity
        theta = self.theta
        phi = self.phi

        
        option1 = self.ff.render("Length=   "+str(round(length)),True,self.fg,self.bg)
        option1_size = option1.get_size()

        option2 = self.ff.render("Mass=   "+str(round(mass)),True,self.fg,self.bg)
        option2_size = option2.get_size()


        option3 = self.ff.render("Damping coeffiecient=   "+str(round(dampcoef)),True,self.fg,self.bg)
        option3_size = option3.get_size()
        
        option4 = self.ff.render("Gravity=   "+str(round(gravity)),True,self.fg,self.bg)
        option4_size = option4.get_size()

        option5 = self.ff.render("Initial angular displacement=   "+str(theta),True,self.fg,self.bg)
        option5_size = option5.get_size()
        
        option6 = self.ff.render("Initial angular velocity=   "+str(phi),True,self.fg,self.bg)
        option6_size = option5.get_size()
        
        single = self.ff.render("Single Pendulum",True,self.fg,self.special)
        single_size = single.get_size()
        double = self.ff.render("Double Pendulum",True,self.fg,self.special)
        double_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2,450,300,40),border_top_right_radius=5,border_bottom_right_radius=5)

        pos1 = length/10
        pos2 = mass/100
        pos3 = dampcoef
        pos4 = gravity
        pos5 = (theta/pi)*100
        pos6 = phi/10
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if save_rect.collidepoint(event.pos):
                        self.length = length
                        self.mass = mass
                        self.dampcoef = dampcoef
                        self.gravity = gravity
                        self.theta = theta
                        self.phi = phi
                        self.run1()
                    if double_rect.collidepoint(event.pos):
                        self.menu_of_two_pendulum()
                        
                # all the keys and control. 
            # body
            clock.tick(60)
            self.window.fill(self.bg)
            self.size = self.window.get_size()

            # rectangle drawing
            pg.draw.rect(self.window,self.fg,(self.size[0]//2-heading_size[0]//2+5,50+5,heading_size[0]+20,heading_size[1]+10),border_radius=5)
            heading_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-heading_size[0]//2,50,heading_size[0]+20,heading_size[1]+10),border_radius=5)
            
            option1_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option1_size[0],130,80,40))
            option2_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option2_size[0],180,80,40))
            option3_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option3_size[0],230,80,40))
            option4_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option4_size[0],280,80,40))
            option5_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option5_size[0],330,80,40))
            option6_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option6_size[0],380,80,40))
            single_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-single_size[0]-50,430,300,40),border_top_left_radius=5,border_bottom_left_radius=5)
            
            double_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2,430,300,40),border_top_right_radius=5,border_bottom_right_radius=5)
            
            
            pg.draw.rect(self.window,self.fg,(self.size[0]//2-200-cancel_size[0]//2+5,self.size[1]-100+5,cancel_size[0]+20,heading_size[1]+10),border_radius=5)
            cancel_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-200-cancel_size[0]//2,self.size[1]-100,cancel_size[0]+20,heading_size[1]+10),border_radius=5)
            pg.draw.rect(self.window,self.fg,(self.size[0]//2+200-save_size[0]//2+5,self.size[1]-100+5,save_size[0]+20,save_size[1]+10),border_radius=5)
            save_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2+200-save_size[0]//2,self.size[1]-100,save_size[0]+20,save_size[1]+10),border_radius=5)

       


            pos1 = self.slider(self.size[0]//2+option1_size[0],130+20,pos1)
            length = (pos1/100)*1000

            pos2 = self.slider(self.size[0]//2+option1_size[0],180+20,pos2)
            mass = (pos2/100)*10000

            pos3 = self.slider(self.size[0]//2+option1_size[0],230+20,pos3)
            dampcoef = (pos3/10000)*100

            pos4 = self.slider(self.size[0]//2+option1_size[0],280+20,pos4)
            gravity = (pos4/100)*100

            pos5 = self.slider(self.size[0]//2+option1_size[0],330+20,pos5)
            theta = (pos5/100)*pi-pi

            pos6 = self.slider(self.size[0]//2+option1_size[0],380+20,pos6)
            phi = (pos6/100)*100
            

            option1 = self.ff.render("Length=   "+str(round(length)),True,self.fg,self.bg)
            option2 = self.ff.render("Mass=   "+str(round(mass)),True,self.fg,self.bg)
            option3 = self.ff.render("Damping Coeffiecient=   "+str(round(dampcoef,5)),True,self.fg,self.bg)
            option4 = self.ff.render("gravity=   "+str(round(gravity)),True,self.fg,self.bg)
            option5 = self.ff.render("Initial angular displacement=   "+str(round(theta,5)),True,self.fg,self.bg)
            option6 = self.ff.render("Initial angular velocity=   "+str(round(phi)),True,self.fg,self.bg)
            
            # blitting
            self.window.blit(heading,(heading_rect.x+10,heading_rect.y+5))
            self.window.blit(option1,option1_rect)
            self.window.blit(option2,option2_rect)
            self.window.blit(option3,option3_rect)
            self.window.blit(option4,option4_rect)
            self.window.blit(option5,option5_rect)
            self.window.blit(option6,option6_rect)
            self.window.blit(single,(single_rect.x+30,single_rect.y+3))
            pg.draw.rect(self.window,self.fg,(self.size[0]//2,430,5,40))
            self.window.blit(double,(double_rect.x+40,double_rect.y+3))
            self.window.blit(cancel,(cancel_rect.x+10,cancel_rect.y+5))
            self.window.blit(save,(save_rect.x+10,save_rect.y+5))

            pg.display.flip()
            # pygame quit 
        pg.quit()


    def menu_of_two_pendulum(self):
        run = True
        clock = pg.time.Clock()
        user_text = '0'

        self.size = self.window.get_size()
        heading = self.ff2.render("Menu for Two Pendulums",True,self.fg,self.special)
        heading_size = heading.get_size()


        save = self.ff2.render("save",True,self.fg,self.special)
        save_size = save.get_size()
        save_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2+200-save_size[0]//2,self.size[1]-100,save_size[0]+20,save_size[1]+10),border_radius=5)

        exit = self.ff2.render("X",True,self.fg,self.special)
        exit_size = save.get_size()
        exit_rect = pg.draw.rect(self.window,self.special,(self.size[0],50,save_size[0]+20,save_size[1]+10),border_radius=5)


        length1 = self.length
        length2 = self.length
        mass1 = self.mass
        mass2 = self.mass
        dampcoef1 = self.dampcoef
        dampcoef2 = self.dampcoef
        
        option11 = self.ff.render("Length=   "+str(round(length1)),True,self.fg,self.bg)
        option12 = self.ff.render("Length=   "+str(round(length2)),True,self.fg,self.bg)
        option1_size = option11.get_size()

        option21 = self.ff.render("Mass=   "+str(round(mass1)),True,self.fg,self.bg)
        option22 = self.ff.render("Mass=   "+str(round(mass2)),True,self.fg,self.bg)
        option2_size = option21.get_size()


        option31 = self.ff.render("Damping coeffiecient=   "+str(round(dampcoef1)),True,self.fg,self.bg)
        option32 = self.ff.render("Damping coeffiecient=   "+str(round(dampcoef2)),True,self.fg,self.bg)
        option3_size = option31.get_size()


        
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
                if event.type == pg.KEYDOWN:
                    if event.key ==pg.K_ESCAPE:
                        run =False
                        break

                if event.type == pg.MOUSEBUTTONDOWN:
                    if save_rect.collidepoint(event.pos):
                        run = False
                        break
                    
            # here

            clock.tick(60)
            self.window.fill(self.bg)


            heading_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-heading_size[0]//2,50,heading_size[0]+20,heading_size[1]+10),border_radius=5)
            
            option11_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option1_size[0],150,80,40))
            option21_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option2_size[0],250,80,40))
            option31_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option3_size[0],350,80,40))

            
            option12_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option1_size[0],150,80,40))
            option22_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option2_size[0],250,80,40))
            option32_rect = pg.draw.rect(self.window,self.bg,(self.size[0]//2-option3_size[0],350,80,40))
            
            save_rect = pg.draw.rect(self.window,self.special,(self.size[0]//2-save_size[0]//2,self.size[1]-100,save_size[0]+20,save_size[1]+10),border_radius=5)
            exit_rect = pg.draw.rect(self.window,self.special,(self.size[0],50,save_size[0]+20,save_size[1]+10),border_radius=5)




            option11 = self.ff.render("Length=   "+str(round(length1)),True,self.fg,self.bg)
            option12 = self.ff.render("Length=   "+str(round(length2)),True,self.fg,self.bg)

            option21 = self.ff.render("Mass=   "+str(round(mass1)),True,self.fg,self.bg)
            option22 = self.ff.render("Mass=   "+str(round(mass2)),True,self.fg,self.bg)

            option31 = self.ff.render("Damping coeffiecient=   "+str(round(dampcoef1)),True,self.fg,self.bg)
            option32 = self.ff.render("Damping coeffiecient=   "+str(round(dampcoef2)),True,self.fg,self.bg)

            self.window.blit(heading,(heading_rect.x+10,heading_rect.y+5))
            self.window.blit(option11,option11_rect)
            self.window.blit(option12,option12_rect)
            self.window.blit(option21,option21_rect)
            self.window.blit(option22,option22_rect)
            self.window.blit(option31,option31_rect)
            self.window.blit(option32,option32_rect)
            self.window.blit(save,(save_rect.x+10,save_rect.y+5))


            
            pg.display.flip()
        
        
    def run1(self):
        run = True
        clock = pg.time.Clock()
        pen = Pendulum(self.length,self.mass,self.dampcoef,self.gravity*980,self.theta,self.phi,image="bitmap1.png")

        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
                if event.type == pg.KEYDOWN:
                    if event.key==pg.K_ESCAPE:
                        run = False
                        break
            # main loop 
            clock.tick(60)
            self.window.fill(self.bg)
            origin = (self.window.get_size()[0]//2,100)
            pen.draw(self.window,origin)
            pen.update()
            pg.display.flip()


    def run2(self):
        run = True
        clock = pg.time.Clock()
        
        pen1 = Pendulum(self.length,self.mass,self.dampcoef,self.gravity,self.theta,self.phi,color="#000000",image="bitmap1.png")
        pen2 = PendulumAppro(self.length,self.mass,self.dampcoef,self.gravity,self.theta,self.phi,image="bitmap2.png",color="#333333")
        length = "length"
        mass = "mass"
        dampcoeff = "damping"
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
k.menu()
