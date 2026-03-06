#!/bin/bash
# Helper script to activate environment and start the app

# source virtualenv if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

streamlit run app.py
