import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
def  Plot(X):
    x=X[0]
    y=X[1]
    z=X[2]
    X_o=[0,0,0]
    l0=2.5
    l1=7.4
    l2=11.4
    t1=math.atan2(y,x)
    c=((x-l0*math.cos(t1))**2+(y-l0*math.sin(t1))**2+z**2)**0.5
    B=math.acos((-l2**2+l1**2+c**2)/(2*l1*c))
    t2=math.asin(-z/c)-B
    C1=math.pi/2-B
    h=l1*math.sin(B)
    C2=math.acos(h/l2)
    t3=math.pi-C1-C2
    T=[[1,t1],[2,t2],[3,t3]]
    x1=X_o[0]
    y1=X_o[1]
    z1=X_o[2]
    x2=l0*math.cos(t1)
    y2=l0*math.sin(t1)
    z2=0
    x3=(l0+l1*math.cos(t2))*math.cos(t1)
    y3=(l0+l1*math.cos(t2))*math.sin(t1)
    z3=-l1*math.sin(t2)
    x4=(l0+l2*math.cos(t3+t2)+l1*math.cos(t2))*math.cos(t1)
    y4=(l0+l2*math.cos(t3+t2)+l1*math.cos(t2))*math.sin(t1)
    z4=-l1*math.sin(t2)-l2*math.sin(t3+t2)
    x_a=[x1,x2,x3,x4]
    y_a=[y1,y2,y3,y4]
    z_a=[z1,z2,z3,z4]
    o = [1 for n in range(len(x_a))]
    o[0]=o[0]+9
    print(o)
    ax.scatter(x_a, y_a, z_a,s=o)
    ax.plot([x1,x2],[y1,y2],[z1,z2],linewidth=0.3)
    ax.plot([x2,x3],[y2,y3],[z2,z3],linewidth=0.3)
    ax.plot([x3,x4],[y3,y4],[z3,z4],linewidth=0.3)

def trajectory_calc(a, b,mod_zyx=(0, 0, 0), right=True, samples=10, debug=True):
    t = np.linspace(0, a, samples)
    x = [t_ + mod_zyx[0] for t_ in t]
    z = [(1 if right else -1) * (b - ((4*b)/(a**2))*((t_-a/2)**2)) + mod_zyx[1] for t_ in t]
    y = [(1 if right else 1) * (b - ((4*b)/(a**2)) * ((t_-a/2)**2) + mod_zyx[2]) for t_ in t]
    if debug:
        mpl.rcParams['legend.fontsize'] = 10
        fig_ = plt.figure()
        ax_ = fig_.gca(projection='3d')
        ax_.plot(*(x, y, z), label='curve')
        ax_.legend()
        plt.show(block=True)
    return ([x, y, z])


temp=trajectory_calc(15,10,(-5,-15,0),debug=False, samples=20)
x=temp[0][5:15]
y=temp[1][5:15]
z=temp[2][5:15]
error=0

for i in range(len(x)):
    a=[x[i],y[i],z[i]]
    try:
        Plot(a)
    except:
        error+=1
    try:
        ax.plot([x[i],x[i+1]],[y[i],y[i+1]],[z[i],z[i+1]])
    except:
        pass
print(error)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
