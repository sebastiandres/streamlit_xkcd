import streamlit as st
import pandas as pd

def get_translation_dict(filepath):
    df = pd.read_csv(filepath, sep=";")
    LANGUAGE_DICT = {}
    keyword = df.columns[0] 
    for L in df.columns[1:]:
        LANGUAGE_DICT[L] = dict(zip(df[keyword], df[L]))
    return LANGUAGE_DICT

def translate(key):
    """Translates the key to the selected language.
    """
    SLANG = st.session_state['SLANG']
    SLANG_DICT = LANGUAGE_DICT[SLANG]
    if key in SLANG_DICT:
        return SLANG_DICT[key]
    else:
        print(f"TRANSLATE KEYWORD {key}")
        if SLANG=="ESP":
            return f"{key} sin traducción"
        else:
            return f"{key} not translated"

LANGUAGE_DICT = get_translation_dict("languages.csv")