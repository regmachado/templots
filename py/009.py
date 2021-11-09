import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['figure.figsize'  ] = (3.3,2.0)
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

x  = np.linspace(0,1,100)
y  = x**2

fig, ax = plt.subplots(nrows=1, ncols=1)

ax.plot(x, y)

ax.set_xlabel(r'$\cos~\theta$')
ax.set_ylabel(r'$x$ (kpc)')  
ax.label_outer()
ax.set_xlim(0,1)
ax.set_xticks(np.arange(0,1.2,0.2))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.set_ylim(0,1)
ax.set_yticks(np.arange(0.2,1.0,0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

#secondary x axis on top
def func(th):
    return np.cos(np.radians(th))

ax2 = ax.twiny()
newlabel = [90,75,60,45,30,0]
newpos   = [func(x) for x in newlabel]
ax2.set_xticks(newpos)
ax2.set_xticklabels(newlabel)
ax2.set_xlabel(r'$\theta~(\degree)$')
ax2.set_xlim(ax.get_xlim())

fig.tight_layout(pad=0.1)    
fig.subplots_adjust(hspace=0.00, wspace=0.0)

plt.savefig('../pdf/009.pdf')
plt.savefig('../png/009.png', dpi=200)
