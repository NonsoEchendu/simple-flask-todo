from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage for todos
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6070)
