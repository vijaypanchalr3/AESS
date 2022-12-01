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
    fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
    # add a big axes, hide frame
    fig.add_subplot(111, frameon=False)
    
    # hide tick and tick label of the big axes
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    # plt.grid(False)
    plt.xlabel("time")
    plt.ylabel("angular displacement")
    plt.title("angualar displacement with time")
    time  = np.linspace(0,total_time,1002)

    # fig.add_subplot(411,frameon=False)
    # ax1 = plt.subplot(111)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    theta_initial = pi/10
    soll = linear_linear(theta_initial,total_time,int(1000/total_time))
    soln = nonlinear_linear(theta_initial,total_time,int(1000/total_time))
    plt.plot(time,soll)
    
    plt.show()

