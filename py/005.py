import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['figure.figsize'  ] = (3.3,2.2)
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
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.sin(3*x)
y4 = np.cos(x)
y5 = np.cos(2*x)
y6 = np.cos(3*x)


fig, ( (ax1, ax2, ax3), (ax4, ax5, ax6) ) = plt.subplots(nrows=2, ncols=3)

Colors = ['tab:red', 'tab:green', 'tab:blue', 'tab:orange', 'tab:brown', 'tab:pink']
lw = 1

ax1.plot(x, y1, lw=lw, color=Colors[0])
ax2.plot(x, y2, lw=lw, color=Colors[1])
ax3.plot(x, y3, lw=lw, color=Colors[2])
ax4.plot(x, y4, lw=lw, color=Colors[3])
ax5.plot(x, y5, lw=lw, color=Colors[4])
ax6.plot(x, y6, lw=lw, color=Colors[5])

for ax in (ax1, ax2, ax3):
    ax.axhline(y=0.0, color='gray', linestyle='--', lw=0.5, zorder=0)

for ax in (ax4, ax5, ax6):
    ax.axvline(x=2.0, color='gray', linestyle=':', lw=0.5, zorder=0)

for ax in fig.get_axes():
    ax.set_xlabel(r'$r$ (kpc)')  
    ax.set_ylabel(r'$\rho_{\rm gas}~({\rm M}_{\odot}\,{\rm kpc}^{-3})$')
    ax.label_outer()
    ax.set_xlim(0,10)
    ax.set_ylim(-2,2)
    ax.set_xticks(np.arange(0,10,2))
    ax.set_yticks([-1,0,1])
    ax.xaxis.set_minor_locator(MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax6.set_xticks(np.arange(0,12,2))

Labels = ['a', 'b', 'c', 'd', 'e', 'f']
for ax, label, color in zip(fig.get_axes(), Labels, Colors):
    ax.annotate(label, xy=(0.92, 0.92), xycoords='axes fraction', ha='right', va='top', color=color)

ax1.annotate('C1', xy=(0.5, 1.1), xycoords='axes fraction', color='k', ha='center', va='bottom')
ax2.annotate('C2', xy=(0.5, 1.1), xycoords='axes fraction', color='k', ha='center', va='bottom')
ax3.annotate('C3', xy=(0.5, 1.1), xycoords='axes fraction', color='k', ha='center', va='bottom')
ax3.annotate('R1', xy=(1.1, 0.5), xycoords='axes fraction', color='k', ha='left', va='center')
ax6.annotate('R2', xy=(1.1, 0.5), xycoords='axes fraction', color='k', ha='left', va='center')

fig.tight_layout(pad=0.1)    
fig.subplots_adjust(hspace=0.00, wspace=0.0)

plt.savefig('../pdf/005.pdf')
plt.savefig('../png/005.png', dpi=200)
