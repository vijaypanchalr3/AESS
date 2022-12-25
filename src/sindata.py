from numpy import sin, pi


with open("sindata.txt","w") as file:
    theta = pi
    for i in range(10):
        file.write("sin(t)= "+str(sin(theta))+"\tfor t="+str(theta)+",\terror="+str(sin(theta)-theta)+"\n")
        theta = theta/5
