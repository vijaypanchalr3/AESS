from main import *
import pygame
import time
from numpy import cos, sin, pi


# this part done.
# just do - [ ] dual color balls



def bob1(window,x,y):
    image = pygame.image.load("./imgs/bitmap1.png")
    window.blit(image, (x,y))

def bob2(window,x,y):
    image = pygame.image.load("./imgs/bitmap2.png")
    window.blit(image, (x,y))

def surface(window,x,y):
    image = pygame.image.load("./imgs/surface.png")
    window.blit(image, (x, y))


    
def position(l,theta):
    return origin_x-10+l*cos((1.5*pi)-theta),origin_y-10-l*sin((1.5*pi)-theta)
    
def mainloop(window,fps):
    global t
    run = True
    clock = pygame.time.Clock()
    c = 0
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
        clock.tick(fps)

        x,y = position(l,exact[c])
        if c==len(exact):
            break
        window.fill("#ffffff")
        surface(window,200,origin_y-15)
        pygame.draw.aaline(window,color="#5BDEC1",start_pos=(origin_x,origin_y),end_pos=(x+radius,y+radius))
        
        bob1(window,x,y)
        pygame.display.update()
        c+=1
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((width,height), pygame.NOFRAME)
    exact = nonlinear_linear(theta_initial,phi_initial,300,fps)
    t = time.perf_counter()
    mainloop(window, fps)
