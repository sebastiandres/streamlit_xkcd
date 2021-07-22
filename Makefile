SHELL := /bin/bash


run:
	source venv/bin/activate
	streamlit run streamlit_app.py
	deactivate


install:
	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt
	deactivate


make uninstall:
	rm -rf venv/
