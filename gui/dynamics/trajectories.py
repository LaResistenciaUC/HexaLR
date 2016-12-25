import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


def trajectory_calc(a, b, right=True, samples=10, mod_zyx=(0, 0, 0), debug=True):
    t = np.linspace(0, a, samples)
    x = [t_ + mod_zyx[0] for t_ in t]
    z = [(-1 if right else 1) * (b - ((4*b)/(a**2))*((t_-a/2)**2)) + mod_zyx[1] for t_ in t]
    y = [(1 if right else 1) * (b - ((4*b)/(a**2)) * ((t_-a/2)**2) + mod_zyx[2]) for t_ in t]
    if debug:
        mpl.rcParams['legend.fontsize'] = 10
        fig_ = plt.figure()
        ax_ = fig_.gca(projection='3d')
        ax_.plot(*(x, y, z), label='curve')
        ax_.legend()
        plt.show(block=True)
    return x, y, z

if __name__ == '__main__':
    mpl.rcParams['legend.fontsize'] = 10
    a_ = 4
    b_ = 1.5
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(*trajectory_calc(a_, b_, right=True, mod_zyx=(10, 10, 10)), label='curve')
    ax.legend()
    plt.show()
