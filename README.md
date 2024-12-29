# API for HCMUT Information System Assignment

## Prerequisite
- Download [Python](https://www.python.org/)
- Download [pip](https://pip.pypa.io/en/stable/) 
- Download [Database](https://drive.google.com/file/d/1soTihyI_bozGfv3N-p-WjdjZ568o8Ith/view?usp=drive_link)

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
Since the API use local storage, change the DATABASE variable in CrudAPI/settings.py file 
```bash
'default': {
        'ENGINE': 'mssql',
        'NAME': 'CompanyX',
        'HOST': 'LAPTOP-DTATJQED\\SQLEXPRESS', # Change the host name to your local SQL Server host name
        'OPTIONS': {
            'trusted_connection': 'yes',
        },
    }
```

Enter the following command
```bash
cd CrudAPI
```
Then
```bash
py manage.py makemigrations CustomerData
```
If there is any new file created in the 'migrations' folder, delete them. Command
```bash
py manage.py migrate
```

Run server with the command
```bash
py manage.py runserver
```