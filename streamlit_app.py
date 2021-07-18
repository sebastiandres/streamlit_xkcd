from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
from numpy import * #sin, cos, tan, log, exp, etc.

LANGUAGE_DICT = {"ESP": {
                         "parameters_title":'Parámetros',
                         "equation": "Ecuación",
                         "title_text": "Título del gráfico",
                         "title_value": "Mi titulo",
                         "xlabel_text": "Nombre eje x",
                         "ylabel_text": "Nombre eje y",
                         "xmin_text": "Valor mínimo de x",
                         "xmax_text": "Valor máximo de x",
                         "examples": "Ejemplos de funciones",
                         "error_warning": "Se ha producido un error al evaluar la función.",
                         "error_advice": "Por favor, modifica los parámetros e inténtalo de nuevo.",
                         "links_md": """**Enlaces**
* [API de Streamlit](https://docs.streamlit.io/)
* [Código en github](https://github.com/sebastiandres/xkcd_streamlit)

Por [sebastiandres](https://linktr.ee/sebastiandres) el 2021-07-08

Inspirado en [http://xkcdgraphs.com/](http://xkcdgraphs.com/)
"""
                        },
                 "ENG": {
                         "parameters_title":'Parameters',
                         "equation": "Equation examples",
                         "title_text": "Title",
                         "title_value": "My Custom Title",
                         "xlabel_text": "x label",
                         "ylabel_text": "y label",
                         "xmin_text": "x min",
                         "xmax_text": "x max",
                         "examples": "Examples",
                         "error_warning": "Error when evaluating the function!",
                         "error_advice": "Please fix and try again.",
                         "links_md": """**Links**
* [Streamlit API](https://docs.streamlit.io/)
* [Code in github](https://github.com/sebastiandres/xkcd_streamlit)

By [sebastiandres](https://linktr.ee/sebastiandres) on 2021-07-08

Inspired on [http://xkcdgraphs.com/](http://xkcdgraphs.com/)
"""

                        },
                }

st.set_page_config(
    page_title="Streamlit & XKCD",
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
print(LANGUAGE_DICT.keys())
SELECTED_LANGUAGE = st.sidebar.selectbox('', list(LANGUAGE_DICT.keys()))
SLANG_DICT = LANGUAGE_DICT[SELECTED_LANGUAGE]
st.sidebar.subheader(SLANG_DICT["parameters_title"])
f = st.sidebar.text_input(SLANG_DICT["equation"],"sin(5*x)/x")
title = st.sidebar.text_input(SLANG_DICT["title_text"], SLANG_DICT["title_value"])
xlabel = st.sidebar.text_input(SLANG_DICT["xlabel_text"], "x")
ylabel = st.sidebar.text_input(SLANG_DICT["ylabel_text"], "y")
xmin = st.sidebar.number_input(SLANG_DICT["xmin_text"], value=-5)
xmax = st.sidebar.number_input(SLANG_DICT["xmax_text"], value=+5)
Nx = 1000
with st.sidebar.beta_expander(SLANG_DICT["examples"]):
    st.code("abs((x+4)*x)")
    st.code("exp(-x**2)")

st.sidebar.markdown(SLANG_DICT["links_md"])
# The main view
try:
    fig = xkcd_plot(f, title, xlabel, ylabel, xmin, xmax, Nx)
    st.pyplot(fig)
except:
    st.error(SLANG_DICT["error_warning"])
    st.warning(SLANG_DICT["error_advice"])
