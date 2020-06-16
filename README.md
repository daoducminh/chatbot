# ChatBot Project - Team18

## Prerequisite

- Python virtual environment: `pip3 install virtualenv`

## Installation

- In root folder, run:
```shell
virtualenv .virtualenvs/
.virtualenvs/bin/python -m pip install .
```
- Create `.env` file with configurations:
```
FLASK_APP=flaskr/app.py
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
FLASK_ENV=development
FLASK_DEBUG=0
MONGODBURI=mongodb://localhost:27017/
```

## Usage

- Preprocess data: `.virtualenvs/bin/python preprocess_data.py`
- Train model: `.virtualenvs/bin/python train_model.py`
- Start server: `.virtualenvs/bin/python -m flask run`
- For modifying Flask environment variables, check out `.env` file.