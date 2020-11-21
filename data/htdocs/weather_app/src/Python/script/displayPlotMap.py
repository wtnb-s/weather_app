import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sys, const

# 日較差算出
def getDailyRange(data):
    # 欠測値を置換
    data = data.replace(-999.0, np.nan)
    dailyRange = data['MaxTemp'] - data['MinTemp']
    return dailyRange.replace(np.nan, -999.0)

# 回帰係数算出
def getRegression(value, year):
    # 欠測値を線形補完
    value = value.interpolate(kind='liner')
    # numpy用に変換
    X_test = year.values.reshape(-1, 1)
    Y_test = value.values.reshape(-1, 1)
    # 回帰係数計算
    rgs = LinearRegression()
    rgs.fit(X_test, Y_test)
    return rgs.coef_

# 平均値算出
def getMean(value):
    return value.mean()

if __name__ == "__main__":
    # コマンドライン引数取得
    args= sys.argv
    fromYear = int(args[1])
    toYear = int(args[2])
    month = int(args[3])
    variable = args[4]
    analysisType = args[5]

    # 計算結果リスト初期化
    valueList = []
    # 都市ファイル読み込み
    cityList = pd.read_csv(const.DATA_PATH_CITY, header=0)
    for city in cityList['city_alpha']:
        # 値取得
        dataAll =  pd.read_csv(const.DATA_PATH_WEATHER + city + ".csv", header=0, encoding='cp932')
        data = dataAll.query("Year >= %s & Year <= %s & Month == %s"%(fromYear, toYear, month))

        if (variable == 'DailyRange'):
            # 日較差計算
            value = getDailyRange(data)
        else:
            value = data[variable]

        # 初期値に欠損値を入力
        analysisData = -999
        # 計算期間の10%以上が欠測値の場合、計算を行わず欠測値とする
        if ((value == -999.0).sum() <= round(len(value)*0.1)):
            # 欠測値をnanに置換
            value = value.replace(-999.0, np.nan)
            if (analysisType == 'mean'):
                analysisData = getMean(value)
            elif (analysisType == 'regression'):
                analysisData = getRegression(value, data['Year'])

        # 計算結果リストに格納
        valueList.append(analysisData)
  
    # 計算結果リストを都市リストにマージ
    displayData = pd.concat([cityList, pd.Series(valueList)], axis=1).rename(columns={0: 'value'})

    # 計算結果ありデータと欠測値データを分けて格納
    displayDataNoValue = displayData.query('value == -999')
    displayDataExistValue = displayData.query('value != -999')

    # 作図処理
    # カラーマップ作成
    cm = plt.cm.get_cmap('rainbow')
    # 降水量を指定した場合のみ、カラーマップを変更
    if (variable == 'Precip'):
        cm = plt.cm.get_cmap('gist_rainbow')
    # figure作成
    plt.figure()
    # 地図ファイル読み込み
    df = gpd.read_file(const.DATA_PATH_MAP_JAPAN)
    # 地図表示
    with plt.style.context("ggplot"):
        df.plot(figsize=(5, 5), edgecolor='#444', facecolor='white', linewidth = 0.7)
        plt.xlim([126,147])
        plt.ylim([25.5,46])

    # プロット
    mappable = plt.scatter(displayDataExistValue['lon'], displayDataExistValue['lat'], c=displayDataExistValue['value'], marker='o', s=12, cmap=cm, alpha=0.9, linewidths = 0.5, edgecolors='black')
    plt.scatter(displayDataNoValue['lon'], displayDataNoValue['lat'], marker='o', s=12, color="gray", alpha=0.9, linewidths = 0.5, edgecolors='black')
    
    # カラーバーを付加
    plt.colorbar(mappable)

    # 画像出力
    outputImage = const.TMP_IMG
    imagePath = const.IMG_PATH + outputImage
    plt.savefig(imagePath, format="png", dpi=150, bbox_inches='tight', pad_inches=0)

    # コントローラーへの返り値
    print(outputImage)