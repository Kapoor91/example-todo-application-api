[![Build Status](https://travis-ci.org/Oltho/example-todo-application-api.svg?branch=master)](https://travis-ci.org/Oltho/example-todo-application-api)
[![codecov.io](https://codecov.io/gh/Oltho/example-todo-application-api/branch/master/graphs/badge.svg)](https://codecov.io/gh/Oltho/example-todo-application-api)

# Example Todo application - API
API part of the todo application, using connexion framework following the OpenAPI 3.0 specification

# How to use
## Prerequisites
python 3.7+

## Installing It
Create a virtual environment (optionnal)

```bash
virtualenv venv
# or
python -m venv venv
```

Install project requirements

```bash
pip install -r requirements.txt
```
## Running it
Run an instance of the server on the default host (127.0.0.1) and port (8000)

```bash
python manage.py runserver
```

If you want your application to listen on another IP/PORT please refer to: 
```python manage.py runserver -h```

## Configuration file
### Local/Development
Copy the local configuration file template

```bash
cp config/conf_local.py.dist config/conf_local.py
```

Update `config/conf_local.py` file with desired configuration.

### Production
Please refer to the `config/conf.py` file. And set environment variable to match the configuration file.

Note that **production** configuration file will be used by default.

Depending on the environnment variable `TODO_APP_API_ENV`, the following file will be used

| TODO_APP_API_ENV  | config file |
| ---------- | ---------- |
| DEVELOPMENT | conf_local.py |
| TESTING | conf_testing.py |
| other | conf_prod.py |

## Running Test
We will run unit testing and code quality with the following command:

```bash
pytest
flake8
```

Test can also be run inside a new virtual environnment by using the command:

```bash
tox
```

## Docker
Docker image can be build for this application by using the given Dockerfile
When running the image please setup the environnment variable required by the `conf_prod.py` configuration file.
