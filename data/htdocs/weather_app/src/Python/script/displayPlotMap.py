import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn import linear_model
import sys, const

def getTrend(year, value):
    clf = linear_model.LinearRegression()
    clf.fit(year, value)
    print(clf.coef_)

def getDailyRange(values):
    return values['MaxTemp'] - values['MinTemp']

if __name__ == "__main__":
    # コマンドライン引数取得
    args= sys.argv
    year = int(args[1])
    month = int(args[2])
    variable = args[3]

    # 都市ファイル読み込み
    cityList = pd.read_csv(const.DATA_PATH_CITY, header=0)
    value = []
    for city in cityList['city_alpha']:
        # 値取得
        data =  pd.read_csv(const.DATA_PATH_WEATHER + city + ".csv", header=0, encoding='cp932')
        values = data.query("Year == %s & Month == %s"%(year, month))
        # 欠測値を置換
        values = values.replace(-999.0, np.nan)

        # 日較差を指定している場合、計算してから格納する
        if (variable == 'DailyRange'):     
            value.append(getDailyRange(values))
        else:
            value.append(values[variable])

    # カラーマップ作成
    cm = plt.cm.get_cmap('rainbow')  
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
    mappable = plt.scatter(cityList['lon'], cityList['lat'], c=value, marker='o', s=12, cmap=cm, alpha=0.9, linewidths = 0.5, edgecolors='black' 	)
    # カラーバーを付加
    plt.colorbar(mappable)

    # 画像出力
    outputImage = const.TMP_IMG
    imagePath = const.IMG_PATH + outputImage
    plt.savefig(imagePath, format="png", dpi=150, bbox_inches='tight', pad_inches=0)

    # コントローラーへの返り値
    print(outputImage)