from flask import Flask, render_template, request
import pandas as pd

data = pd.read_excel('data.xlsx', usecols='B,C,D,E,F,G')
data

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080)