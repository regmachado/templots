import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import stats
from scipy.ndimage import gaussian_filter
from pylab import ma
import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

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

ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])
fig.add_axes(ax)
ax.set_axis_off()

im = plt.imshow(Z.T, extent=extent, origin='lower', cmap='viridis', interpolation='nearest', vmin=vmin, vmax=vmax)


#scale bar
fontprops = fm.FontProperties(size=8)
scalebar = AnchoredSizeBar(ax.transData,
                    100, '100 kpc', 'lower right', 
                    pad=0.2,
                    color='white',
                    frameon=False,
                    size_vertical=0.02,
                    fontproperties=fontprops)
ax.add_artist(scalebar)

#color bar
cax= inset_axes(ax, width='84%', height='4%', loc='upper center') 
cb = fig.colorbar(im, cax=cax, orientation='horizontal')
cb.ax.tick_params(direction='in', length=2, labelsize=8, labelcolor='white')
cb.set_label('$kT$ (keV)', fontsize=8, color='white', labelpad=6)
cb.mappable.set_clim(0,10)
cb.set_ticks([2,4,6,8])

ax.set_aspect('equal')
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)

plt.savefig('../pdf/013.pdf')
plt.savefig('../png/013.png', dpi=200)
