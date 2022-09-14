from numpy import cos, sin, arange, sqrt, zeros, exp
import matplotlib.pyplot as plt

gamma, m, l, g = 0, 0.1, 1, 9.8
F = g/l



def K2(theta,phi):
    return -((gamma/m)*phi)-(F*sin(theta))
def N_ODE_RK4(t,theta,phi):
    h = 0.1
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

# w = arange(0,100,1)
sol = zeros([102])
sol2 = zeros([102])
sol[0] = 3.141592
sol2[0] = 3.141592
t,phi = zeros([102]),0
c=0
while c<100:
    t[c+1], sol[c+1], phi = N_ODE_RK4(t[c],sol[c],phi)
    sol2[c+1]=exp(-gamma*t[c]*0.5)*cos(sqrt(F)*t[c])*sol2[0]
    print(sol2[c])
    c+=1
plt.plot(sol)
plt.plot(sol2)
plt.show()
