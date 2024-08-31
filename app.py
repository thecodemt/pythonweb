# app.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to my simple Python web application."

@app.route('/api/data')
def get_data():
    # 返回一些示例数据
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)