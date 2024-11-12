from flask import Flask, render_template, request

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return render_template('result.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)