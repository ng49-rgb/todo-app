# Flask Todo App

A simple Flask + SQLAlchemy todo application with create, update, delete, and search features.

## Features
- Add new tasks
- Update existing tasks
- Delete tasks
- Search tasks by title
- Display dates in dd-mm-yyyy format

## DEMO LINK: https://todo-app-o1n9.onrender.com/

## Requirements
blinker==1.9.0
click==8.4.2
colorama==0.4.6
Flask==3.1.3
Flask-SQLAlchemy==3.1.1
greenlet==3.5.3
gunicorn==26.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
packaging==26.2
SQLAlchemy==2.0.51
typing_extensions==4.16.0
Werkzeug==3.1.8


## Setup
1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open http://127.0.0.1:5000

## Tests
Run the tests with:
```bash
python -m unittest tests.test_app -v
```
