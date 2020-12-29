from flask import Flask, request, Response
from flask_cors import CORS
from codes import getLineGraph, getPlotMap

app = Flask(__name__)
model = None

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/apiGetLineGraph", methods=['GET'])
# 地点折れ線グラフ画像取得
def callLineGraph():
    params = request.args
    city = params.get('city') if 'city' in params else ''
    month = params.get('month') if 'month' in params else ''
    variable = params.get('variable') if 'variable' in params else ''
    runningMeanPeriod = params.get('runningMeanPeriod') if 'runningMeanPeriod' in params else 0
    if (city != '' and month != '' and variable != ''):
        result = getLineGraph.main(city, int(month), variable, int(runningMeanPeriod))
        if (result):
            f = open('/api/img/tmp.png', 'rb')
            image = f.read()
            return Response(response=image, content_type='image/png')
    return 'no image'

@app.route("/apiGetPlotMap", methods=['GET'])
# プロット地図画像取得
def callPlotMap():
    params = request.args
    fromYear = params.get('fromYear') if 'fromYear' in params else ''
    toYear = params.get('toYear') if 'toYear' in params else ''
    month = params.get('month') if 'month' in params else ''
    variable = params.get('variable') if 'variable' in params else ''
    analysisType = params.get('analysisType') if 'analysisType' in params else ''
    if (fromYear != '' and toYear != '' and month != '' and variable != '' and analysisType != ''):
        result = getPlotMap.main(int(fromYear), int(toYear), int(month), variable, analysisType)
        if (result):
            f = open('/api/img/tmp.png', 'rb')
            image = f.read()
            return Response(response=image, content_type='image/png')
    return 'no image'