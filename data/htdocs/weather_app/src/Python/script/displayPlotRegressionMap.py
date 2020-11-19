import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sys, const

def getDailyRange(values):
    return values['MaxTemp'] - values['MinTemp']

if __name__ == "__main__":
    # コマンドライン引数取得
    args= sys.argv
    year = int(args[1])
    month = int(args[2])
    variable = args[3]

    coefList = []
    # 都市ファイル読み込み
    cityList = pd.read_csv(const.DATA_PATH_CITY, header=0)
    for city in cityList['city_alpha']:
        # 初期値に欠損値を入力
        coef = -999
        # 値取得
        data =  pd.read_csv(const.DATA_PATH_WEATHER + city + ".csv", header=0, encoding='cp932')
        values = data.query("Month == %s"%(month))
        if ((values[variable] == -999.0).sum() <= 10):
            # 欠測値を線形補完
            value = values[variable].replace(-999.0, np.nan).interpolate(kind='liner')    
            # numpy用に変換
            X_test = values['Year'].values.reshape(-1, 1)
            Y_test = value.values.reshape(-1, 1)
            # 回帰係数計算
            rgs = LinearRegression()
            rgs.fit(X_test, Y_test)
            coef = rgs.coef_

        # 係数リストに格納
        coefList.append(coef)
  
    # 係数リストを都市リストにマージし、欠測値都市と結果有り年に分ける
    list1 = pd.concat([cityList, pd.Series(coefList)], axis=1).rename(columns={0: 'coef'})
    cityListNoValue = list1.query('coef == -999')
    cityListExistValue = list1.query('coef != -999')

    # カラーマップ作成
    cm = plt.cm.get_cmap('rainbow')  
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
    mappable = plt.scatter(cityListExistValue['lon'], cityListExistValue['lat'], c=cityListExistValue['coef'], marker='o', s=12, cmap=cm, alpha=0.9, linewidths = 0.5, edgecolors='black')
    plt.scatter(cityListNoValue['lon'], cityListNoValue['lat'], marker='o', s=12, color="gray", alpha=0.9, linewidths = 0.5, edgecolors='black')
    
    # カラーバーを付加
    plt.colorbar(mappable)

    # 画像出力
    outputImage = const.TMP_IMG
    imagePath = const.IMG_PATH + outputImage
    plt.savefig(imagePath, format="png", dpi=150, bbox_inches='tight', pad_inches=0)

    # コントローラーへの返り値
    print(outputImage)