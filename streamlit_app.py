from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
from numpy import * #sin, cos, tan, log, exp

"""
# XKCD-style Graphs
You can use functions as sin, cos, tan, log, exp, and others.
"""

def xkcd_plot(f, title, xlabel, ylabel, xmin, xmax, Nx):
    # Based on "Stove Ownership" from XKCD by Randall Munroe
    # https://xkcd.com/418/
    with plt.xkcd():
        # Create the figure
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        # No idea what this is
        ax.spines.right.set_color('none')
        ax.spines.top.set_color('none')
        # Eval the data
        x = np.linspace(xmin, xmax, num=Nx) + 1E-16 # So if we divide by x no errors
        y = eval(f)
        # Plot
        ax.plot(x, y)
        # Set the limits for the plot
        ymin = int(np.floor(y.min())-1)
        ymax = int(np.ceil(y.max())+1)
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

if True:
    f = st.text_input("Equation","x*sin(x)")
    title = st.text_input("Title","My title")
    xlabel = st.text_input("x-label","x")
    ylabel = st.text_input("y-label","y")
    xmin = st.number_input("x min", -10)
    xmax = st.number_input("x max", +10)
    Nx = 1000
    try:
        fig = xkcd_plot(f, title, xlabel, ylabel, xmin, xmax, Nx)
        st.pyplot(fig)
    except:
        st.markdown("# Error evaluating the function.")
        st.markdown("## Please fix and try again")
"""
### Links: 
* [Streamlit API](https://docs.streamlit.io/)
* [Code in github](https://github.com/sebastiandres/xkcd_streamlit)

By [sebastiandres](https://linktr.ee/sebastiandres) on 2021-07-08, inspired on [http://xkcdgraphs.com/](http://xkcdgraphs.com/).
"""
