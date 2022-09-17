from numpy import arange
import main
import matplotlib.pyplot as plt



exact = main.nonlinear(1,20)
appro = main.linear(1,20)
i = arange(0,1+2/1200,1/1200)

plt.plot(i,appro)
plt.plot(i,exact)
plt.show()






