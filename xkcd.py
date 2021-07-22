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
        x = np.linspace(xmin, xmax, num=Nx) + 1E-16 # So if we divide by x no errors
        y_list = []
        for f, c in f_list:
            y = eval(f)
            # Plot
            ax.plot(x, y, color=c)
            y_list.append(y)
        y = np.array(y_list)
        # Set the limits for the plot
        if len(f_list)>0:
            ymin = int(np.floor(y.min())-1)
            ymax = int(np.ceil(y.max())+1)
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
