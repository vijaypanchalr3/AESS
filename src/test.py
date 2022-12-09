from numpy import linspace, exp

def accuracy(RK,fps):
    acc = {1:0,10: 0,100: 0}
    f2 = lambda a,b:a
    x, p = 1, -1
    for i in linspace(0,1,fps):
        x,p = RK(x,p,1/fps,f2)
    acc[1] = x
    x, p = 1, -1
    for i in linspace(0,10,10*fps):
        x,p = RK(x,p,1/fps,f2)
    acc[2] = x
    x, p = 1, -1
    for i in linspace(0,100,100*fps):
        x,p = RK(x,p,1/fps,f2)
    acc[3] = x
    acc[1],acc[2],acc[3] = exp(-1)-acc[1],exp(-10)-acc[2],exp(-100)-acc[100]
    print("Error at 1 sec ",acc[1],", 10 sec ",acc[10],", 100 sec ",acc[100]," in ",fps,"%d")
    return 0




