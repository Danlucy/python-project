from flask import Flask, jsonify, request

from database import User, UserDatabase
from database import Book, BookDatabase


print("Starting server")

userDB = UserDatabase()
userDB.loadFromFile()
userDB.check()

bookDB = BookDatabase()
bookDB.loadFromFile()
#bookDB.saveToFile()
bookDB.check()
# Create Flask app
app = Flask(__name__)

# Sample data (dictionary)
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'This is task 1.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'This is task 2.',
        'done': False
    }
]

# GET route to fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# POST route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)  # Bad request

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201  # Created

# GET route to fetch a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)  # Not found
    return jsonify({'task': task[0]})

# PUT route to update a task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)  # Not found
    if not request.json:
        abort(400)  # Bad request
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)  # Bad request
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)  # Bad request
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)  # Bad request

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# DELETE route to delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)  # Not found
    tasks.remove(task[0])
    return jsonify({'result': True})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

