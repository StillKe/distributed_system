from flask import Flask, request, jsonify
from tasks import process_data

app = Flask(__name__)

@app.route('/')
def home():
    return "Worker node is running."

@app.route('/perform_task', methods=['POST'])
def perform_task():
    task_data = request.json.get('task_data')
    result = process_data(task_data)
    return jsonify({'result': result})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'Worker node is running'})

if __name__ == "__main__":
    app.run(port=5001)  # Adjust port for different workers
