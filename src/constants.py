from numpy import sin, sqrt, zeros, pi




# defining constants in C.G.S.


width,height = 1360,720         # pygame window size in pixel units
origin_x,origin_y = width/2,height/8 # setting up the origin O

# density
rho = 0.70

# newton's drag coefficient
cd = 0.47

# diameter
d = 20

# mass 
m = 500

# length of string
l = 500

# gravitation accelaration
g = 980

# viscosity of air
eta = 0.0001834

kl = 3*pi*eta*d
kq = (1/8)*pi*cd*rho*d*d

gammal = (kl)/m
gammaq = (kq*l)/m
w0 = sqrt(g/l)                  # natural frequncy of SHM
radius = 10                     # radius of ball in pixel
fps = 120                        # frame per second



# initial conditions
theta_initial = pi/4     # initial theta in radian
phi_initial = 0.0
