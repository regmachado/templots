import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import stats
from scipy.ndimage import gaussian_filter
from pylab import ma

plt.rcParams['figure.figsize'  ] = (3.3,2.6)
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

L      = 500
Nbins  = 64
smooth = 2.0

x = 2*L * np.random.sample(1000) -L
y = 2*L * np.random.sample(1000) -L
Q = 20  * np.random.sample(1000)

def Measure(x, y, Q, Nbins, L, smooth, statistic='mean', log=True):
    results, xb, yb, binnum = stats.binned_statistic_2d(x, y, Q, statistic=statistic, bins=Nbins, range=[[-L,L],[-L,L]])
    extent = [xb[0], xb[-1], yb[0], yb[-1]]
    if (log==True):
        Z = ma.log10( results ) 
        Z = Z.filled( Z.min() ) 
    else:
        Z = 10**ma.log10( results )
        Z = Z.filled( Z.min() ) 
    Z = gaussian_filter(Z, sigma=smooth)
    vmin = Z.min()
    vmax = Z.max()
    return Z, extent, vmin, vmax

Z, extent, vmin, vmax = Measure(x, y, Q, Nbins=Nbins, L=L, smooth=smooth, statistic='mean', log=False)

fig, ax = plt.subplots(nrows=1, ncols=1)

im = plt.imshow(Z.T, extent=extent, origin='lower', cmap='viridis', interpolation='nearest', vmin=vmin, vmax=vmax)

cb = plt.colorbar(im, ax=ax, shrink=1.0, aspect=18, pad=0.03)
cb.mappable.set_clim(0,10)
cb.set_ticks([2,4,6,8])
cb.set_label(r'$kT$ (keV)')

ax.set_xlabel(r'$x$ (kpc)')
ax.set_ylabel(r'$y$ (kpc)')
ax.set_aspect('equal')
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)
ax.set_xticks(np.arange(-400,600,200))
ax.set_yticks(np.arange(-400,600,200))

fig.tight_layout(pad=0.1)    

plt.savefig('../pdf/012.pdf')
plt.savefig('../png/012.png', dpi=200)
