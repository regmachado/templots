import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['figure.figsize'  ] = (3.3,3.3)
plt.rcParams['font.size'       ] = 8
plt.rcParams['legend.fontsize' ] = 8
plt.rcParams['legend.frameon'  ] = False
plt.rcParams['font.family'     ] = 'STIXGeneral'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['xtick.direction' ] = 'in'
plt.rcParams['ytick.direction' ] = 'in'
plt.rcParams['xtick.top'       ] = True
plt.rcParams['ytick.right'     ] = True
plt.rcParams['xtick.major.size'] = 2
plt.rcParams['xtick.minor.size'] = 1
plt.rcParams['ytick.major.size'] = 2
plt.rcParams['ytick.minor.size'] = 1
plt.rcParams['xtick.major.width'] = 0.75
plt.rcParams['xtick.minor.width'] = 0.5
plt.rcParams['ytick.major.width'] = 0.75
plt.rcParams['ytick.minor.width'] = 0.5

x  = np.linspace(1,9,15)
y  = np.sin(x)
z  = y**2 

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

im1 = ax1.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='viridis')
im2 = ax2.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='coolwarm')

for ax in fig.get_axes():
    ax.set_xlabel(r'$x$ (kpc)')  
    ax.set_ylabel(r'$y$ (kpc)')
    ax.set_xlim(0,10)
    ax.set_xticks(np.arange(0,10,2))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_ylim(-2,2)
    ax.set_yticks([-1,0,1])
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    ax.label_outer()

cb1 = fig.colorbar(im1, ax=ax1, shrink=0.98, aspect=15, pad=0.02)
cb2 = fig.colorbar(im2, ax=ax2, shrink=0.98, aspect=15, pad=0.02)

cb1.set_label(r'$t$ (Gyr)', labelpad=4)
cb2.set_label(r'$t$ (Gyr)', labelpad=8)

cb1.set_ticks([0.25,0.5,0.75])
cb2.set_ticks(np.arange(0.2,1.0,0.2))

fig.tight_layout(pad=0.1)    
fig.subplots_adjust(hspace=0.00, wspace=0.0)

plt.savefig('../pdf/006.pdf')
plt.savefig('../png/006.png', dpi=200)
