from flask import Flask, render_template, make_response

import json
from candle.candle_crawling import CandleController
from flask_cors import CORS

from change_ratio.get_change_ratio import get_change_ratio
from news.read_csv import ReadCsvCreateForWordcloud
from new_magic_formula.model import Recommendation_Stock_Model
from realtime_stock_data.realtime_data_to_json_by_symbol import RealtimeController
from datetime import datetime, timedelta
import time
from time import time
from random import random

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r'/**': {"origins": "*"}})
CORS(app, supports_credentials=True)
CORS_ALLOW_ORIGIN = "*,*"
CORS_EXPOSE_HEADERS = "*,*"
CORS_ALLOW_HEADERS = "content-type,*"
cors = CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(","),
            expose_headers=CORS_EXPOSE_HEADERS.split(","), supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# @app.route('/')
# def hello_world():
#     return render_template('index.html')


@app.route('/recommendation/<period>/<propensity>', methods=['GET'])
def recommend_stock(period, propensity):
    period = period
    propensity = propensity
    print(period, propensity)
    recommend_stock_model = Recommendation_Stock_Model()
    return json.dumps(recommend_stock_model.recommendation_listing(period=period, propensity=propensity))


@app.route('/wordcloud', methods=['GET'])
def create_wordcloud_using_csv():
    c = ReadCsvCreateForWordcloud()
    result = c.read()
    print(result)
    return result


@app.route('/stocks/candle/<symbol>', methods=['GET'])
def get_candle(symbol):
    symbol = symbol
    tmp = CandleController()
    app_result = tmp.candle_crawling(symbol=symbol)
    return json.dumps(app_result)


CORS(app)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', threaded=True)
