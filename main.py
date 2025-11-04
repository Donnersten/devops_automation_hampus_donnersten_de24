from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    num1 = 5 
    num2 = 10
    return num1 + num2

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
