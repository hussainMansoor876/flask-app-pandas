from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

data = pd.read_excel('data.xlsx', usecols='B,C,D,E,F,G')


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    dict1 = {}
    req = dict(request.form)
    print(req)
    for i in data:
        ind = random.randint(0, int(len(data[i].dropna())-1))
        dict1[i] = data[i][ind]
    return jsonify({"result": dict1})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
