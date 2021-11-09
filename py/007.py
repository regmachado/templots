import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.rcParams['figure.figsize'  ] = (7.0,3.5)
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

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)

im1 = ax1.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='viridis')
im2 = ax2.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='viridis')
im3 = ax3.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='viridis')
im4 = ax4.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='viridis')
im5 = ax5.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='viridis')
im6 = ax6.scatter(x, y, c=z, vmin=0.0, vmax=1.0, cmap='viridis')

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

fig.subplots_adjust(right=0.9)
cax = fig.add_axes([0.9, 0.09, 0.025, 0.9])
cb  = plt.colorbar(im1, cax=cax, pad=0)

cb.set_label(r'$\log~(M_\star~/~{\rm M}_{\odot})$', labelpad=12)
cb.set_ticks(np.arange(0,0.9,0.2))

fig.subplots_adjust(left=0.055, bottom=0.09, top=0.99, right=0.9, hspace=0.00, wspace=0.0)

plt.savefig('../pdf/007.pdf')
plt.savefig('../png/007.png', dpi=200)
