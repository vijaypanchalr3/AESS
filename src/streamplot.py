from numpy import linspace, meshgrid
from main import *
import matplotlib.pyplot as plt


def exact_lineardamp():
    x1 = linspace(-6,6,2000)
    x2 = linspace(-6,6,2000)

    x1_,x2_ = meshgrid(x1,x2)

    u,v = nonlinear_phase_plane(x1_,x2_)
    vel = sqrt(u**2+v**2)

    plt.figure()
    plt.streamplot(x1_,x2_,u,v, color='k', linewidth=0.8,density=1.5, minlength=0.01, arrowsize=0.8,arrowstyle="->")
    plt.title("stream plot of equation without approximation")
    plt.xlabel("$\theta$")
    plt.ylabel("$\phi$")
    plt.savefig("../graphs/exactlstr.png")

def appro_lineardamp():
    x1 = linspace(-6,6,2000)
    x2 = linspace(-6,6,2000)

    x1_,x2_ = meshgrid(x1,x2)

    u,v = linear_phase_plane(x1_,x2_)
    vel = sqrt(u**2+v**2)

    plt.figure()
    plt.streamplot(x1_,x2_,u,v, color='k', linewidth=0.8,density=1.5, minlength=0.01, arrowsize=0.8,arrowstyle="->")
    plt.title("stream plot of approximated equation")
    plt.xlabel("$\theta$")
    plt.ylabel("$\phi$")
    plt.savefig("../graphs/approlstr.png")

exact_lineardamp()
appro_lineardamp()
