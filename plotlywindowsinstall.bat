@echo off
echo Starting Installation of Plotly.py
::opens anaconda terminal
call %USERPROFILE%\Anaconda3\Scripts\activate.bat
::create virtual environment for plotly.py
cd plotly.py
call conda create -n plotly-dev python -y
call conda activate plotly-dev
:: install requirements
echo Installing text requirements
call pip install -r packages/python/plotly/requirements.txt
call pip install -r packages/python/plotly/optional-requirements.txt