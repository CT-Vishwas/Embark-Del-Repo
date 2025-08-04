from flask import Flask, jsonify, request

app = Flask(__name__)

# In memory
tasks = [
    {"id": 1, "title":"Python Advanced", "done": False},
    {"id": 2, "title": "Flask", "done": False}
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Untitled Task"),
        "done": False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True)
