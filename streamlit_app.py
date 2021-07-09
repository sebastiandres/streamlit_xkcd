from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
from numpy import * #sin, cos, tan, log, exp

st.set_page_config(
    page_title='XKCD-style plots with streamlit',
    layout="wide",
    initial_sidebar_state="expanded",
)

def xkcd_plot(f, title, xlabel, ylabel, xmin, xmax, Nx):

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

# The side bar
st.sidebar.markdown("**Parameters**")
f = st.sidebar.text_input("Equation","sin(5*x)/x")
title = st.sidebar.text_input("Title","My title")
xlabel = st.sidebar.text_input("x label","x")
ylabel = st.sidebar.text_input("y label","y")
xmin = st.sidebar.number_input("x min", value=-5)
xmax = st.sidebar.number_input("x max", value=+5)
Nx = 1000
st.sidebar.markdown("**Examples**")
st.sidebar.code("abs((x+4)*x)")
st.sidebar.code("exp(-x**2)")

links_md = """**Links**
* [Streamlit API](https://docs.streamlit.io/)
* [Code in github](https://github.com/sebastiandres/xkcd_streamlit)

By [sebastiandres](https://linktr.ee/sebastiandres) on 2021-07-08

Inspired on [http://xkcdgraphs.com/](http://xkcdgraphs.com/)
"""
st.sidebar.markdown(links_md)
# The main view
try:
    fig = xkcd_plot(f, title, xlabel, ylabel, xmin, xmax, Nx)
    st.pyplot(fig)
except:
    st.markdown("# Error evaluating the function.")
    st.markdown("## Please fix and try again")
