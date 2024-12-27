# API for HCMUT Information System Assignment

## Prerequisite
- Download [Python](https://www.python.org/)
- Download [pip](https://pip.pypa.io/en/stable/) 

## Python virtual environment
You can use Python virtual environment using the following command
```bash
python -m venv env
```
Then activate the created virtual environment
- For Windows:
```bash
./env/Scripts/activate.ps1 # if you use Windows PowerShell
```
or 
```bash
./env/Scripts/activate
```
- For MacOS & Linux:
```bash
source ./env/Scripts/activate
```
## Installation
Install the neccessary packages 
```bash
pip install -r requirements.txt
```

## Usage
Apply the following commands in your terminal

```bash
cd CrudAPI
python manage.py runserver
```