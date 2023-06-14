import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib.ticker import FormatStrFormatter
import matplotlib.colors as mcolors
assert 'Times New Roman' in list(sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist]))
# print(matplotlib.matplotlib_fname())

plt.rcParams['font.family'] = 'Times'  # sometimes 'Times New Roman'
plt.rcParams['font.serif'] = ['Times'] + plt.rcParams['font.serif']
plt.rcParams['font.size'] = 15
plt.rcParams['text.usetex'] = True
plt.rcParams['font.weight'] = 'normal'

GLOBAL_FS = 25
LINE_STYLES = ['-', ':', '--', '-.'] #'solid', 'dotted', 'dashed', 'dashdot'
EXTENDED_LINE_STYLES = ['-', ':', '--', '-.', (5, (15, 2)), (0, (5,2,1,2,1,2)), (0, (5,5)), (0, (5,2,1,2,1,2,1,2)),]
MARKER_STYLES = ['o', 's', '^', 'v', 'd', '<', '>', '*', 'p', 'h', 'D', 'X', 'P']
COLOR_STYLES = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'brown', 'pink', 'olive']

def set_ax_thickness(ax, thickness=2):
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(thickness)
        
def set_ax_grid(ax):
    ax.grid(color='black', linestyle=':', linewidth=0.2)
    
def set_ax_ticks(ax, direction, low_bound, high_bound, interval, n_subs=5, fontsize=GLOBAL_FS):
    ticks = np.arange(low_bound, high_bound+interval/2, interval)
    sub_ticks = np.arange(low_bound, high_bound+interval/2/n_subs, interval/n_subs)
    if direction.lower() == 'x':
        ax.set_xticks(ticks, fontsize=fontsize)
        ax.set_xticks(sub_ticks, minor=True, fontsize=fontsize)
    elif direction.lower() == 'y':
        ax.set_yticks(ticks, fontsize=fontsize)
        ax.set_yticks(sub_ticks, minor=True, fontsize=fontsize)
    set_ax_labelsize(ax, fontsize)
    
def set_ax_labelsize(ax, labelsize=GLOBAL_FS):
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(labelsize)
        
def set_ax_ticks_styles(ax, labelsize=GLOBAL_FS, ticklength=10, tickwidth=2, tickdirection='in', ticksboth=True):
    ticklocs = {"bottom": True, "top": True, "left": True, "right": True}
    ax.tick_params(axis='both', which='major', labelsize=labelsize, 
                   length=ticklength, width=tickwidth, direction=tickdirection,
                   **ticklocs)
    ax.tick_params(axis='both', which='minor', labelsize=labelsize, 
                   length=ticklength/2, width=tickwidth, direction=tickdirection,
                   **ticklocs)
    
