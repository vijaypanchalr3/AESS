from main import *
import pygame
import time


def bob1(window,x,y):
    image = pygame.image.load("bitmap1.png")
    window.blit(image, (x,y))

def bob2(window,x,y):
    image = pygame.image.load("bitmap2.png")
    window.blit(image, (x,y))

def surface(window,x,y):
    image = pygame.image.load("surface.png")
    window.blit(image, (x, y))


    
# origin_x1 = origin_x-200

# origin_x2 = origin_x+200


def position1(l,theta):
    return origin_x-radius+l*cos((1.5*3.141598)-theta),origin_y-radius-l*sin((1.5*3.14159)-theta)

# def position2(l,theta):
    # return origin_x2-radius+l*cos((1.5*3.141598)-theta),origin_y-radius-l*sin((1.5*3.14159)-theta)

def mainloop(window,fps):
    global t
    run = True
    clock = pygame.time.Clock()
    c = 0
    window.fill("#FBDEC1")
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
        clock.tick(fps)

        x,y = position1(l,exact[c])
        # x2,y2 = position2(l,appro[c])
        if c==len(exact):
            break
        window.fill("#ffffff")
        surface(window,200,origin_y-15)
        pygame.draw.aaline(window,color="#5BDEC1",start_pos=(origin_x,origin_y),end_pos=(x+radius,y+radius))
        # pygame.draw.aaline(window,color="#5BDEC1",start_pos=(origin_x2,origin_y),end_pos=(x2+radius,y2+radius))
        bob1(window,x,y)
        # bob2(window,x2,y2)
        pygame.display.update()
        c+=1
    pygame.quit()
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((width,height))
    exact = nonlinear(2,fps)
#    appro = linear(5,20)
    t = time.perf_counter()
    mainloop(window, fps)
