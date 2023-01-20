from main import *
from numpy import linspace, meshgrid,zeros,pi,sqrt,size,arange
import matplotlib.pyplot as plt


def exact_lineardamp():
    t = arange(0,20,0.01)
    x1 = linspace(-6,6,2000)
    x2 = linspace(-6,6,2000)

    x1_,x2_ = meshgrid(x1,x2)

    u,v = linear_phase_plane(t,x1_,x2_)
    vel = sqrt(u**2+v**2)

    plt.figure()
    plt.streamplot(x1_,x2_,u,v, color='k', linewidth=0.8,density=2, minlength=0.1)
    plt.title("stream plot of equation without approximation")
    plt.xlabel("$\theta$")
    plt.ylabel("$\phi$")
    plt.show()

exact_lineardamp()
