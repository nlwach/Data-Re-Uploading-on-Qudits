import qutip as q
from qutip import spin_q_function
from qutip import Qobj

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
import matplotlib.pyplot as plt

import numpy as np

def plot_bloch(state, qudit_num=2, azim=None, elev=None):
    
    thetas = np.linspace(0, np.pi, 100)
    phis = np.linspace(0, 2*np.pi, 100)
    
    density, _, _  = spin_q_function(Qobj(state), thetas, phis)

    thetam, phim = np.meshgrid(thetas,phis);

    x = 1 * np.sin(thetam) * np.cos(phim)
    y = 1 * np.sin(thetam) * np.sin(phim)
    z = 1 * np.cos(thetam)


    fig = plt.figure(figsize=(15, 11))
    ax = fig.add_subplot(111, projection='3d')

    strength = density
    norm=colors.Normalize(vmin = np.min(strength),
                          vmax = np.max(strength), clip = False)

    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False,
                           facecolors=cm.coolwarm(norm(density)))
    
    ax.text(0, 0, -1.3, rf"$|{0}\rangle$")
    ax.text(0, 0, 1.2, rf"$|{qudit_num}\rangle$")
    ax.view_init(azim, elev)