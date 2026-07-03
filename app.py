from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


def format_date(value):
    if value is None:
        return ""
    return value.strftime('%d-%m-%Y')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.globals['format_date'] = format_date

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        desc = request.form.get('desc', '').strip()
        if title:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
    all_todos = Todo.query.order_by(Todo.date_created.desc()).all()
    return render_template('index.html', allTodo=all_todos)


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if todo is None:
        return redirect('/')

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        desc = request.form.get('desc', '').strip()
        if title:
            todo.title = title
            todo.desc = desc
            db.session.commit()
        return redirect('/')

    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if todo is not None:
        db.session.delete(todo)
        db.session.commit()
    return redirect('/')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_term = ''
    if request.method == 'POST':
        search_term = request.form.get('search', '').strip()
    else:
        search_term = request.args.get('search', '').strip()

    if search_term:
        todos = Todo.query.filter(
            Todo.title.contains(search_term)
        ).order_by(Todo.date_created.desc()).all()
    else:
        todos = []

    return render_template('search.html', todos=todos, search_query=search_term)


if __name__ == "__main__":
    app.run(debug=True)