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

x  = np.linspace(1,9,100)
y  = np.sin(x)

fig, ax = plt.subplots(nrows=1, ncols=1)

ax.plot(x, y, label='C1')
ax.plot(x, y-0.5, label='C2')

#legend color
leg = ax.legend(handlelength=0, loc='upper right')
for line,text in zip(leg.get_lines(), leg.get_texts()):
    text.set_color(line.get_color())

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
fig.subplots_adjust(hspace=0.00, wspace=0.00)

plt.savefig('../pdf/000.pdf')
plt.savefig('../png/000.png', dpi=200)
