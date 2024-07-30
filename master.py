from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# List of worker nodes
WORKER_NODES = [
    'http://localhost:5001',
    'http://localhost:5002'
]

@app.route('/task', methods=['POST'])
def distribute_task():
    task = request.json.get('task')
    results = []
    
    for node in WORKER_NODES:
        response = requests.post(f"{node}/perform_task", json={'task': task})
        results.append(response.json())
    
    return jsonify(results)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'Master node is running'})

if __name__ == "__main__":
    app.run(port=5000)