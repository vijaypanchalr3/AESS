from constants import *
from numpy import arange, exp, sin, cos, size, sqrt, zeros, pi

# phi = arctan(gamma/2)
# A = theta_initial/cos(phi)
# w = sqrt((w0*w0)-((gamma*gamma)/4))



def f2nonlinear(theta,phi):
    return -((gamma/m)*phi*phi)-(w0*sin(theta))

def f2linear(theta,phi):
    return -((gamma/m)*phi*phi)-(w0*theta)

def N_ODE_RK4(t,theta,phi,h,K):
    h = h/8
    for i in range(8):
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
        t+=h
        theta+=k_
        phi+=l_
    return  t,theta,phi
    
def linear(Total_time,fps):
    linear_solutions = zeros([Total_time*fps+2])
    linear_solutions[0] = theta_initial
    phi = zeros([Total_time*fps+2])
    phi[0],t,time = 0,0,0
    while t<Total_time*fps:
        time, linear_solutions[t+1], phi[t+1] = N_ODE_RK4(time,linear_solutions[t],phi[t],1/fps,f2linear)
        t+=1
    return linear_solutions

def nonlinear(Total_time,fps):
    nonlinear_solutions = zeros([Total_time*fps+2])
    nonlinear_solutions[0] = theta_initial
    phi = zeros([Total_time*fps+2])
    phi[0],t,time = 0,0,0
    while t<Total_time*fps:
        time, nonlinear_solutions[t+1], phi[t+1] = N_ODE_RK4(time,nonlinear_solutions[t],phi[t],1/fps,f2nonlinear)
        t+=1
    return nonlinear_solutions

def w_nonliner(theta_initial):
    T = (sqrt(l/g))*(1+(0.24*(sin(0.5*theta_initial))**2)+((9/24)*(sin(theta_initial*0.5))**4))
    return 1/T
CNPF1 = 2*w0/(1+4*gamma*gamma)
CNPF2 = -(4*w0*gamma)/(1+4*gamma*gamma)

def nonlinear_phase_fun(theta,c):
    return sqrt(c*exp(-2*gamma*theta)+CNPF1*cos(theta)+CNPF2*sin(theta))

def phase_plane(fun,space,deviation,c):
    theta = arange(-space,space,deviation)
    size = int(2*space/deviation)
    phi = zeros([size])
    for i in range(size):
        phi[i] = fun(c,theta[i])    
    return theta,phi
