# ChatBot Project - Team18

## Installation

- In root folder, run:
```shell
mkdir .virtualenvs
python3 -m venv .virtualenvs/
.virtualenvs/bin/pip3 install .
```
- Create `.env` file with configurations:
```
FLASK_APP=flaskr/app.py
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
FLASK_ENV=development
FLASK_DEBUG=0
```

## Usage

- In root folder, run: `flask run`
- For modifying Flask environment variables, check out `.env` file.