#!/bin/bash
cd ~
echo Starting Installation of Plotly
#Activates conda
source .bashrc
#Creates virtual environment
conda create -n plotly-dev python -y
conda activate plotly-dev