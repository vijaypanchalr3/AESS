from math import sqrt

# defining constants in C.G.S.


width,height = 1360,720         # pygame window size in pixel units
origin_x,origin_y = width/2,height/8 # setting up the origin O
b = 100                              # damping coefficient
m = 100                              # 100 grams of mass
l = 100                              # 100 cm length
g = 980                              # gravitation accelaraiotion in cgs

gamma = b/m

w0 = sqrt(g/l)                  # natural frequncy of SHM
theta_initial = 3.141591/4      # initial theta in radian
radius = 10                     # radius of ball in pixel
fps = 60                        # frame per second
