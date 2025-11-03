from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")  # 'mongo' = service name from docker-compose
db = client.todo_db
todos = db.todos

@app.route('/')
def index():
    items = todos.find()
    return render_template('index.html', todos=items)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    todos.insert_one({'task': task})
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
