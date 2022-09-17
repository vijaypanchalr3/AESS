from constants import *
from numpy import sin, cos, zeros, pi

# phi = arctan(gamma/2)
# A = theta_initial/cos(phi)
# w = sqrt((w0*w0)-((gamma*gamma)/4))

def f2nonlinear(theta,phi):
    return -((gamma/m)*phi)-(w0*sin(theta))

def f2linear(theta,phi):
    return -((gamma/m)*phi)-(w0*theta)

def N_ODE_RK4(t,theta,phi,h,K):
    k1 = h*phi
    l1 = h*K(theta,phi)
    k2 = h*(phi+(l1*0.5))
    l2 = h*(K(theta+(k1*0.5),phi+(l1*0.5)))
    k3 = h*(phi+(l2*0.5))
    l3 = h*(K(theta+(k2*0.5),phi+(l2*0.5)))
    k4 = h*(phi+l3)
    l4 = h*(K(theta+k3,phi+l3))
    k_ = (1/6)*(k1+k4+2*(k2+k3))
    l_ = (1/6)*(l1+l4+2*(l2+l3))
    return  t+h,theta+k_,phi+l_
    
def linear(Total_time,fps):
    linear_solutions = zeros([Total_time*60*fps+2])
    linear_solutions[0] = theta_initial
    phi = zeros([Total_time*60*fps+2])
    phi[0],t,time = 0,0,0
    while t<Total_time*60*fps:
        time, linear_solutions[t+1], phi[t+1] = N_ODE_RK4(time,linear_solutions[t],phi[t],1/60,f2linear)
        t+=1
    return linear_solutions

def nonlinear(Total_time,fps):
    nonlinear_solutions = zeros([Total_time*60*fps+2])
    nonlinear_solutions[0] = theta_initial
    phi = zeros([Total_time*60*fps+2])
    phi[0],t,time = 0,0,0
    while t<Total_time*60*fps:
        time, nonlinear_solutions[t+1], phi[t+1] = N_ODE_RK4(time,nonlinear_solutions[t],phi[t],1/60,f2nonlinear)
        t+=1
    return nonlinear_solutions

