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
::Installation of plotly packages
echo Installing editable plotly packages
call pip install -e packages/python/plotly/
call pip install -e packages/python/chart-studio/
call pip install -e packages/python/plotly-geo/
echo Installing editable plotly packages completed
::Jupyter Notebook Support
echo Installing Jupyter Notebook Support
call conda install "notebook>=5.3" "ipywidgets=7.5" -y
::Ipywidgets development install
echo Installing Ipywidgets
call jupyter nbextension enable --py widgetsnbextension
call jupyter nbextension install --py --symlink --sys-prefix plotlywidget
call jupyter nbextension enable --py --sys-prefix plotlywidget
