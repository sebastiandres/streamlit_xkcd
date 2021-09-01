import streamlit as st
from xkcd import xkcd_plot
from shared import translate, LANGUAGE_DICT

# Set page properties for the app
st.set_page_config(
    page_title="Streamlit & XKCD",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize the session states - f_list has functions and colors
if 'f_list' not in st.session_state:
	st.session_state['f_list'] = [
                                  ("5*exp(-x**2)", "g"),
                                  ("sin(5*x)/x", "b"),
                                 ]
if 'SLANG' not in st.session_state:
	st.session_state['SLANG'] = list(LANGUAGE_DICT.keys())[0]

# The side bar
language_title = st.sidebar.empty() # Hack so the title gets updated before selection is made
st.session_state['SLANG'] = st.sidebar.selectbox("", 
                                                 list(LANGUAGE_DICT.keys())
                                                 )
language_title.subheader(translate("language_title"))

# Delete
SLANG_DICT = LANGUAGE_DICT[st.session_state['SLANG']]

st.sidebar.subheader(translate("parameters_title"))

with st.sidebar.expander(translate("functions_expander")):
    f = st.text_input(translate("equation"), "sin(5*x)/x")
    c = st.color_picker(translate("function_color"), "#0000FF")
    col1, col2 = st.columns(2)
    if col1.button(translate("add_function")):
        st.session_state['f_list'].append( (f, c) )
    if col2.button(translate("clean_functions")):
        st.session_state['f_list'] = []
    st.write(translate("functions_link"))

with st.sidebar.expander(translate("graph_expander")):
    title = st.text_input(translate("title_text"), translate("title_value"))
    xlabel = st.text_input(translate("xlabel_text"), "x")
    ylabel = st.text_input(translate("ylabel_text"), "y")
    xmin = st.number_input(translate("xmin_text"), value=-5)
    xmax = st.number_input(translate("xmax_text"), value=+5)

st.sidebar.markdown(translate("links_md"))

# The main view
try:
    fig = xkcd_plot(st.session_state['f_list'], title, xlabel, ylabel, xmin, xmax, Nx=1001)
    st.pyplot(fig)
except Exception as e:
    st.session_state['f_list'] = []
    st.error(translate("error_warning"))
    st.warning(translate("error_advice"))
    st.exception(e)