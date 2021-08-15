import pickle
import random
from flask import Flask, request, jsonify, json, Response
import pandas as pd
from imports import Stats_translate, Store_translate, Product_translate

with open("model.pkl", 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__)

HOSTNAME = "http://localhost:3000"


@app.route('/')
def main():
    return "NOTHING HERE"


@app.route('/add', methods=['POST'])
def collect():
    # data
    data = json.loads(request.data.decode("utf-8").replace("'", '"'))

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df['product_id'] = df['product_id'].astype(int)
    df['store_id'] = df['store_id'].astype(int)
    print(df)
    predicted = model.predict(df)
    response = app.response_class(response=json.dumps({'answer': predicted[0]}),
                                  status=200,
                                  mimetype='application/json'
                                  )
    response.headers['Access-Control-Allow-Origin'] = HOSTNAME
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
