from main import *
import numpy as np
import matplotlib.pyplot as plt




def angfre():
    A = np.linspace(-np.pi,np.pi,6000)
    w = np.zeros(np.size(A))
    w0 = np.zeros(np.size(A))

    for i in range(np.size(A)):
        w[i] = w_nonliner(A[i])
        w0[i] = np.sqrt(g/l)

    
    plt.figure()
    plt.plot(A,w, label="angular frequency of nonlinear solution")
    plt.plot(A,w0, label="angular frequency of linear solution")
    plt.title("angular frequency")
    plt.ylabel("angular frequency")
    plt.xlabel("initial displacement")
    plt.legend()
    plt.savefig("angfre.png")
    plt.close
    
def thetawitht(total_time):
    fig = plt.figure()
    # fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)
    gs = fig.add_gridspec(2, 2)
    (ax1, ax2), (ax3, ax4) = gs.subplots()

    fig.suptitle('Angular displacement vs time t')
    # plt.xlabel("time")
    # plt.ylabel("angular displacement")

    time  = np.linspace(0,total_time,1002)



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
    plt.savefig("thetawitht.png")
    plt.close()


angfre()
thetawitht(40)



    
