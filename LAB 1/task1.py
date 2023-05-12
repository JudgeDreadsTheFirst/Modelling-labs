import numpy as np
import matplotlib.pyplot as plt 
import math 
def plotter(N,x):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data',t0))
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x,N,'r')

    plt.show()

def free_pop(n0,t0,t,r):
    N = []
    x = np.linspace(t0,t,t-t0)
    for i in range(int(t0),int(t)):
        N.append(n0*math.exp(r*(i-t0)))
    
    plotter(N,x)

def limit_pop(n0,t0,t,r,b):
    N1 = []
    N2 = []
    k = r/b
    x = np.linspace(t0,t,t-t0)
    for i in range(int(t0),int(t)):
        N1.append(n0*math.exp(r*(i-t0)))
        N2.append((k*N1[i-t0])/(k + N1[i-t0] - n0))

    plotter(N2,x)    

def resource_pop(n0,t0,t,r,b,c,h):
    k = r/b
    F = []
    N3 = []
    t = t 
    x = np.linspace(t0,t,t-t0+1)
    N3.append(n0)
    F.append(h)
    print(F[0])
    for i in range(int(t0),int(t)):
        N3.append(N3[i-t0]+((r*N3[i-t0])*(1-N3[i-t0]/(k*F[i-t0]))))
        F.append(F[i-t0]+(c-b*N3[i-t0+1]))
    plotter(N3,x)  

print("Enter starting population number")
N0 = input()
N0 = int(N0)
print("Enter start time")
t0 = input()
t0 = int(t0)
print("Enter end time(must be greater than start time)")
t = input()
t = int(t)
print("Enter r coefficient")
r = input()
r = float(r)
print("Enter b coefficient")
b = input()
b = float(b)
print("Enter c coefficient")
c = input()
c = float(c)
print("Enter f resource starting number")
f = input()
f = float(f)

free_pop(N0,t0,t,r)
limit_pop(N0,t0,t,r,b)
resource_pop(N0,t0,t,r,b,c,f)