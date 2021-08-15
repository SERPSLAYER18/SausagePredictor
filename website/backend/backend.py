from flask import Flask, request, jsonify, json, Response
import random

# from flask_cors import CORS

app = Flask(__name__)

HOSTNAME = "http://localhost:3000"


# CORS(app)


@app.route('/')
def main():
    return "NOTHING HERE"


@app.route('/add', methods=['POST'])
def collect():
    # data
    data = request.data.decode("utf-8")
    response = app.response_class(response=json.dumps({'answer': str(random.randint(3, 42))}),
                                  status=200,
                                  mimetype='application/json'
                                  )
    response.headers['Access-Control-Allow-Origin'] = HOSTNAME

    print(response.json)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
