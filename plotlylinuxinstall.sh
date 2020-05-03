#!/bin/bash
cd ~
echo Starting Installation of Plotly
#Activates conda
source .bashrc
#Creates virtual environment
conda create -n plotly-dev python -y
conda activate plotly-dev
#install requirements
echo Installing text requirements
pip install -r packages/python/plotly/requirements.txt
pip install -r packages/python/plotly/optional-requirements.txt
#Installation of plotly packages
echo Installing editable plotly packages
pip install -e packages/python/plotly/
pip install -e packages/python/chart-studio/
pip install -e packages/python/plotly-geo/
echo Installing editable plotly packages completed
