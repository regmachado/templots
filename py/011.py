import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.gridspec import GridSpec

plt.rcParams['figure.figsize'  ] = (3.3,3.0)
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


fig = plt.figure()
gs  = GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 0.4])

ax1 = fig.add_subplot(gs[0, 0:2])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

ax1.plot(x, y, label='C1')
ax2.plot(x, y, label='C2')
ax3.plot(x, y, label='C3')

##legend color
#leg = ax.legend(handlelength=0, loc='upper right')
#for line,text in zip(leg.get_lines(), leg.get_texts()):
    #text.set_color(line.get_color())


for ax in [ax1, ax2, ax3]:
    #ax.label_outer()
    ax.set_xlim(0,10)
    ax.set_xticks(np.arange(0,10,2))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_ylim(-2,2)
    ax.set_yticks([-1,0,1])
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))

ax1.set_xlabel(r'$x_1$ (kpc)')  
ax2.set_xlabel(r'$x_2$ (kpc)')
ax3.set_xlabel(r'$x_3$ (kpc)')

ax1.set_ylabel(r'$y_1$ (kpc)')  
ax2.set_ylabel(r'$y_2$ (kpc)')
ax3.set_ylabel(r'$y_3$ (kpc)')

plt.tight_layout(pad=0.1)    
plt.subplots_adjust(hspace=0.5, wspace=0.5)

plt.savefig('../pdf/011.pdf')
plt.savefig('../png/011.png', dpi=200)
