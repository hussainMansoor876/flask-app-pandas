from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

data = pd.read_excel('data.xlsx', usecols='B,C,D,E,F,G')
dict1 = {}

app = Flask(__name__)


@app.route('/')
def index():
    for i in data:
        ind = random.randint(0, int(len(data[i].dropna())-1))
        dict1[i] = data[i][ind]
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    req = dict(request.form)
    print(req)
    return render_template('result.html', req=req, dict1=dict1, keys=data.columns)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
