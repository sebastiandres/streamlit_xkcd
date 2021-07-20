from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
from numpy import * #sin, cos, tan, log, exp, etc.

LANGUAGE_DICT = {"ESP": {
                         "parameters_title":'Parámetros',
                         "functions_expander":'Funciones',
                         "add_function":'Agregar función',
                         "clean_functions":'Borrar funciones',
                         "function_color":'Color',
                         "graph_expander":"Propiedades del gráfico",
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
                         "functions_expander":'Functions',
                         "function_color":'Color',
                         "clean_functions":'Delete functions',
                         "add_function":'Add new function',
                         "graph_expander":"Graph configuration",
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

# The side bar
SELECTED_LANGUAGE = st.sidebar.selectbox('', list(LANGUAGE_DICT.keys()))
SLANG_DICT = LANGUAGE_DICT[SELECTED_LANGUAGE]
st.sidebar.subheader(SLANG_DICT["parameters_title"])

# Initialize the session states - f_list has functions and colors
if 'f_list' not in st.session_state:
	st.session_state['f_list'] = [
                                  ("5*exp(-x**2)", "g"),
                                  ("sin(5*x)/x", "b"),
        ]

with st.sidebar.beta_expander(SLANG_DICT["functions_expander"]):
    f = st.text_input(SLANG_DICT["equation"],"sin(5*x)/x")
    c = st.color_picker(SLANG_DICT["function_color"], "#0000FF")
    col1, col2 = st.beta_columns(2)
    if col1.button(SLANG_DICT["add_function"]):
        st.session_state['f_list'].append( (f, c) )
    if col2.button(SLANG_DICT["clean_functions"]):
        st.session_state['f_list'] = []

with st.sidebar.beta_expander(SLANG_DICT["graph_expander"]):
    title = st.text_input(SLANG_DICT["title_text"], SLANG_DICT["title_value"])
    xlabel = st.text_input(SLANG_DICT["xlabel_text"], "x")
    ylabel = st.text_input(SLANG_DICT["ylabel_text"], "y")
    xmin = st.number_input(SLANG_DICT["xmin_text"], value=-5)
    xmax = st.number_input(SLANG_DICT["xmax_text"], value=+5)

st.sidebar.markdown(SLANG_DICT["links_md"])

# The main view
try:
    fig = xkcd_plot(st.session_state['f_list'], title, xlabel, ylabel, xmin, xmax, Nx=1000)
    st.pyplot(fig)
except Exception as e:
    st.error(SLANG_DICT["error_warning"])
    st.warning(SLANG_DICT["error_advice"])
    st.exception(e)
