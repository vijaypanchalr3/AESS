from constants import *
from numpy import cos, sin, arange, sqrt, zeros, exp
import pygame
import time



def blip(window,x,y):
    image = pygame.image.load("bitmap2.png")
    window.blit(image, (x,y))

def blip2(window,x,y):
    image = pygame.image.load("bitmap.png")
    window.blit(image, (x,y))

def K2(theta,phi):
    return -((gamma/m)*phi)-(F*sin(theta))

def N_ODE_RK4(t,theta,phi,h):
    k1 = h*phi
    l1 = h*K2(theta,phi)
    k2 = h*(phi+(l1*0.5))
    l2 = h*(K2(theta+(k1*0.5),phi+(l1*0.5)))
    k3 = h*(phi+(l2*0.5))
    l3 = h*(K2(theta+(k2*0.5),phi+(l2*0.5)))
    k4 = h*(phi+l3)
    l4 = h*(K2(theta+k3,phi+l3))
    k = (1/6)*(k1+k4+2*(k2+k3))
    l = (1/6)*(l1+l4+2*(l2+l3))
    return  t+h,theta+k,phi+l

def nonlinear(Total_time,fps):
    nonlinear_solutions = zeros([Total_time*60*fps+2])
    nonlinear_solutions[0] = theta_initial
    phi = zeros([Total_time*60*fps+2])
    phi[0] = 0
    t = 0
    while t<Total_time*60*fps:
        accurate_s = nonlinear_solutions[t]
        accurate_p = phi[t]
        time = t/(60*fps)
        time, nonlinear_solutions[t+1], phi[t+1] = N_ODE_RK4(time,accurate_s,accurate_p,0.1)
        t+=1
    return nonlinear_solutions

def linear(Total_time,fps):
    linear_solutions = zeros([Total_time*60*fps+2])
    linear_solutions[0] = theta_initial
    t=0
    while t<Total_time*60*fps:
        time = t/(60*fps)
        linear_solutions[t+1]= (1.5*3.14159-linear_solutions[0])+exp(-gamma*time*0.5)*cos(sqrt(F)*time-theta_initial)
        t+=1
    return linear_solutions

def position(l,theta):
    return origin_x+l*cos((1.5*3.141598)-theta),origin_y-l*sin((1.5*3.14159)-theta)
    
def mainloop(window):
    global t
    run = True
    clock = pygame.time.Clock()
    fps = 20
    c = 0
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
        clock.tick(fps)
        window.fill("#ffffff")
        x,y = position(l,exact[c])
        x2,y2 = position(l,appro[c])
        c+=1
        
        # if c<1*120:
            # x,y = movement(0)
            # t = time.perf_counter()
            
        # else:
            # x,y = movement((time.perf_counter()-t)*patience)
        # x,y = position(1,(time.perf_counter()-t))
        blip(window,x,y)
        blip2(window,x2,y2)
        pygame.draw.aaline(window,color="#222222",start_pos=(origin_x,origin_y),end_pos=(x+10,y+10))
        pygame.draw.aaline(window,color="#222222",start_pos=(origin_x,origin_y),end_pos=(x2+10,y2+10))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    # pygame initializatoin and settings
    pygame.init()
    window = pygame.display.set_mode((width,height))
    exact = nonlinear(5,60)
    appro = linear(5,60)
    t = time.perf_counter()
    mainloop(window)
