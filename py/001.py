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

x  = np.linspace(1,9,100)
y  = np.sin(x)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(x, y)
ax2.plot(x, y)

for ax in fig.get_axes():
    ax.set_xlabel(r'$x$ (kpc)')  
    ax.set_ylabel(r'$y$ (kpc)')
    ax.label_outer()
    ax.set_xlim(0,10)
    ax.set_xticks(np.arange(0,10,2))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_ylim(-2,2)
    ax.set_yticks([-1,0,1])
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))

fig.tight_layout(pad=0.1)    
fig.subplots_adjust(hspace=0.00, wspace=0.0)

plt.savefig('../pdf/001.pdf')
plt.savefig('../png/001.png', dpi=200)
