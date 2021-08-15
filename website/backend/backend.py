import pickle
import random
from flask import Flask, request, jsonify, json, Response
import pandas as pd
import numpy as np
from imports import Stats_translate, Store_translate, Product_translate, PredictionChecker

with open("model.pkl", 'rb') as f:
    model = pickle.load(f)
    print(model)
app = Flask(__name__)
pch = PredictionChecker('data/Ядерный_чемоданчик_clear.csv', 15)
HOSTNAME = "http://localhost:3000"
print('OK')


@app.route('/')
def main():
    return "NOTHING HERE"


@app.errorhandler(500)
def internal_error(error):
    response = app.response_class(response=json.dumps({'answer': "ERROR"}),
                                  status=200,
                                  mimetype='application/json'
                                  )
    response.headers['Access-Control-Allow-Origin'] = HOSTNAME
    return response


@app.route('/add', methods=['POST'])
def collect():
    # data
    data = json.loads(request.data.decode("utf-8").replace("'", '"'))
    print("RECEIVED:", data)

    df = pd.DataFrame(data)

    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df['product_id'] = df['product_id'].astype(int)
    df['store_id'] = df['store_id'].astype(int)
    can_predict = pch.check(df['store_id'][0], df['product_id'][0])

    if not can_predict:
        values = str(list(df['sales']))[1:-1].replace('\'', '').split(',')
        values = np.array([float(val) for val in values])
        response = app.response_class(response=json.dumps({'answer': np.mean(values) * 7}),
                                      status=200,
                                      mimetype='application/json'
                                      )
        response.headers['Access-Control-Allow-Origin'] = HOSTNAME
        return response
    predicted = model.predict(df)
    response = app.response_class(response=json.dumps({'answer': predicted[0]}),
                                  status=200,
                                  mimetype='application/json'
                                  )
    response.headers['Access-Control-Allow-Origin'] = HOSTNAME
    #    print(response.json)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
