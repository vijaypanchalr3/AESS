from constants import *


def f2nonlinear_linear(theta,phi):     # we defined second auxillary equation from nonlinear term.
    return -((gammal)*phi)-(w0*sin(theta))

def f2linear_linear(theta,phi):        # we defined second auxillary equation from linear term.
    return -((gammal)*phi)-(w0*theta)

def f2llinear_nonlinear(theta,phi):        # we defined second auxillary equation from linear term.
    return -((gammaq)*phi*phi)-(w0*theta)

def f2nonlinear_nonlinear(theta,phi):        # we defined second auxillary equation from linear term.
    return -((gammaq)*phi*phi)-(w0*sin(theta))



# range-kutta method defined
def RK4(theta,phi,h,K): 
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
        theta+=k_
        phi+=l_
    return theta,phi

# Solutions of linear term ---- gives array of length (Total_time*fps)
def linear_linear(theta_initial,Total_time,fps):
    linear_solutions = zeros([Total_time*fps+2])
    linear_solutions[0] = theta_initial
    phi = zeros([Total_time*fps+2])
    phi[0],t = 0,0
    while t<Total_time*fps:
        linear_solutions[t+1], phi[t+1] = RK4(linear_solutions[t],phi[t],1/fps,f2linear_linear)
        t+=1
    return linear_solutions

def linear_nonlinear(theta_initial,Total_time,fps):
    linear_solutions = zeros([Total_time*fps+2])
    linear_solutions[0] = theta_initial
    phi = zeros([Total_time*fps+2])
    phi[0],t = 0,0
    while t<Total_time*fps:
        linear_solutions[t+1], phi[t+1] = RK4(linear_solutions[t],phi[t],1/fps,f2llinear_nonlinear)
        t+=1
    return linear_solutions

# Solutions of nonlinear term ---- gives array of length (Total_time*fps)
def nonlinear_linear(theta_initial,Total_time,fps):
    nonlinear_solutions = zeros([Total_time*fps+2])
    nonlinear_solutions[0] = theta_initial
    phi = zeros([Total_time*fps+2])
    phi[0],t= 0,0
    while t<Total_time*fps:
        nonlinear_solutions[t+1], phi[t+1] = RK4(nonlinear_solutions[t],phi[t],1/fps,f2nonlinear_linear)
        t+=1
    return nonlinear_solutions

def nonlinear_nonlinear(theta_initial,Total_time,fps):
    nonlinear_solutions = zeros([Total_time*fps+2])
    nonlinear_solutions[0] = theta_initial
    phi = zeros([Total_time*fps+2])
    phi[0],t= 0,0
    while t<Total_time*fps:
        nonlinear_solutions[t+1], phi[t+1] = RK4(nonlinear_solutions[t],phi[t],1/fps,f2nonlinear_nonlinear)
        t+=1
    return nonlinear_solutions

# ------------(for graphs)----------
# this describes frequncy of nonlinear term.
def w_nonliner(theta_initial):
    w_ = (sqrt(l/g))*(1+(0.25*(sin(0.5*theta_initial))**2)+((9/64)*(sin(theta_initial*0.5))**4))
    return 1/w_

# phase plane definations
def linear_phase_plane(theta,phi):
    f1 = phi
    f2 = -((gammal)*phi)-(w0*theta)
    return f1,f2

def nonlinear_phase_plane(theta,phi):
    f1 = phi
    f2 = -((gammal)*phi)-(w0*sin(theta))
    return f1,f2

def linear_phase_planeq(theta,phi):
    f1 = phi
    f2 = -((gammaq)*phi*phi)-(w0*theta)
    return f1,f2

def nonlinear_phase_planeq(theta,phi):
    f1 = phi
    f2 = -((gammaq)*phi*phi)-(w0*sin(theta))
    return f1,f2

# ----------------------------------


if __name__=="__main__":
    # print("plzz,define some tests")
    from test import *
    accuracy(RK4,60)
