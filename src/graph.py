from main import *
from numpy import linspace, meshgrid,zeros,pi,sqrt,size
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

    
def angfre():
    A = linspace(-pi,pi,6000)
    w = zeros(size(A))
    w0 = zeros(size(A))

    for i in range(size(A)):
        w[i] = w_nonliner(A[i])
        w0[i] = sqrt(g/l)

    
    plt.figure()
    plt.plot(A,w, label="angular frequency of nonlinear solution")
    plt.plot(A,w0, label="angular frequency of linear solution")
    plt.title("angular frequency")
    plt.ylabel("angular frequency")
    plt.xlabel("initial displacement")
    plt.legend()
    plt.savefig("../graphs/angfre.png")
    plt.close
    
def thetawitht(total_time):
    fig = plt.figure()
    # fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)
    gs = fig.add_gridspec(2, 2)
    (ax1, ax2), (ax3, ax4) = gs.subplots()

    fig.suptitle('Angular displacement vs time t')
    # plt.xlabel("time")
    # plt.ylabel("angular displacement")

    time  = linspace(0,total_time,1002)



    theta_initial = pi/10
    soll = linear_linear(theta_initial,total_time,int(1000/total_time))
    soln = nonlinear_linear(theta_initial,total_time,int(1000/total_time))
    ax1.plot(time,soll)
    ax1.plot(time,soln)
    ax1.set_title("theta = pi/10")
    # plt.ylabel("angular displacement")


    theta_initial = theta_initial*2
    soll = linear_linear(theta_initial,total_time,int(1000/total_time))
    soln = nonlinear_linear(theta_initial,total_time,int(1000/total_time))
    ax2.plot(time,soll)
    ax2.plot(time,soln)
    ax2.set_title("theta = pi/5")

    theta_initial = pi/2
    soll = linear_linear(theta_initial,total_time,int(1000/total_time))
    soln = nonlinear_linear(theta_initial,total_time,int(1000/total_time))
    ax3.plot(time,soll)
    ax3.plot(time,soln)
    ax3.set_title("theta = pi/2")

    theta_initial = pi
    soll = linear_linear(theta_initial,total_time,int(1000/total_time))
    soln = nonlinear_linear(theta_initial,total_time,int(1000/total_time))
    ax4.plot(time,soll)
    ax4.plot(time,soln)
    ax4.set_title("theta = pi")
    fig.tight_layout()
    plt.savefig("../graphs/thetawitht.png")
    plt.close()


if __name__=="__main__":
    angfre()
    thetawitht(40)
    exact_lineardamp()
    appro_lineardamp()



    
