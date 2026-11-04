@echo off

echo Creating Python virtual environment...
python -m venv .venv

echo Installing Python packages...
.venv\Scripts\python.exe -m pip install -r requirements.txt

echo Starting JupyterLab...
.venv\Scripts\python.exe -m jupyter lab

pause
