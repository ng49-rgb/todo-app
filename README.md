# Flask Todo App

A simple Flask + SQLAlchemy todo application with create, update, delete, and search features.

## Features
- Add new tasks
- Update existing tasks
- Delete tasks
- Search tasks by title
- Display dates in dd-mm-yyyy format

## Requirements
- Python 3.11+
- Flask
- Flask-SQLAlchemy

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
