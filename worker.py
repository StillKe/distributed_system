from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/perform_task', methods=['POST'])
def perform_task():
    task = request.json.get('task')
    result = f"Task '{task}' performed by worker node"
    return jsonify({'result': result})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'Worker node is running'})

if __name__ == "__main__":
    app.run(port=5001)  # Change to 5002 for the second worker