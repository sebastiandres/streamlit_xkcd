from matplotlib import pyplot as plt
import numpy as np
from numpy import * #sin, cos, tan, log, exp, etc.

def xkcd_plot(f_list, title, xlabel, ylabel, xmin, xmax, Nx):

    with plt.xkcd():
        # Create the figure
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        # No idea what this is
        ax.spines.right.set_color('none')
        ax.spines.top.set_color('none')
        # Eval the data
        x = np.linspace(xmin, xmax, num=Nx) # So if we divide by x no errors
        ymin_list, ymax_list = [], []
        for f, c in f_list:
            y = eval(f)
            # Mask infinite values
            y[logical_not(isfinite(y))] = nan 
            # Plot
            ax.plot(x, y, color=c)
            ymin_list.append( int(np.floor(y[isfinite(y)].min())-1) )
            ymax_list.append( int(np.ceil(y[isfinite(y)].max())+1) )
        if len(f_list)>0:
            ymin, ymax = min(ymin_list), max(ymax_list)
        else:
            ymin, ymax = xmin, xmax
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        # Put the x ticks
        if xmin*xmax<0:
            ax.set_xticks([xmin, 0, xmax])
        else:
            ax.set_xticks([xmin, xmax])
        # Put the y ticks
        if ymin*ymax<0:
            ax.set_yticks([ymin, 0, ymax])
        else:
            ax.set_yticks([ymin, ymax])
        # Set text
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        return fig
