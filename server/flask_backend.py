from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import uuid
import datetime

app = Flask(__name__)


@app.route('/task-management')
def task_management():
    return app.send_static_file('website/task_management.html')
 
    return jsonify([]), 200

@app.route('/', methods=['PUT'])
def complete_task(task_id):
    # Logic to mark a task as complete
    return app.send_static_file('website/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
