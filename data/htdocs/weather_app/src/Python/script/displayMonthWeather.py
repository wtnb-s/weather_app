from scipy import interpolate
import os, sys, const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getDailyRange(values):
    return values['MaxTemp'] - values['MinTemp']

if __name__ == "__main__":
    # コマンドライン引数取得
    args= sys.argv
    file = args[1] + ".csv"
    month = int(args[2])
    variable = args[3]
    runningMeanPeriod = int(args[4])
    
    # 値取得
    data =  pd.read_csv(const.DATA_PATH_WEATHER + file, header=0, encoding='cp932')
    values = data[data['Month'] == month]
    # 欠測値を置換
    values = values.replace(-999.0, np.nan)

    # 日較差を指定している場合
    if (variable == 'DailyRange'):
        values['DailyRange'] = getDailyRange(values)
    
    # 作図
    plt.figure(dpi=100, figsize=(7,3))
    plt.plot(values['Year'], values[variable], color="black", linewidth=0.7, linestyle="-", label="")
    
    # 移動平均期間が指定されている場合、移動平均計算
    if(runningMeanPeriod != 0):
        # 欠測値がある場合、線形補完する
        noMissingValue = values[variable].interpolate(kind='liner')
        runningMeanValue = noMissingValue.rolling(window = runningMeanPeriod, center = True).mean()
        plt.plot(values['Year'], runningMeanValue, color="blue", linewidth=1.5, linestyle="-", label="移動平均")
    
    # ラベル、グリッド、トリミング
    plt.xlabel("Year", fontsize=14, fontname='Times New Roman')
    plt.grid()
    plt.subplots_adjust(left=0.1, right=0.98, bottom=0.15, top=0.98)
    
    # 画像出力
    outputImage = const.TMP_IMG
    imagePath = const.IMG_PATH + outputImage
    plt.savefig(imagePath)
    
    # コントローラーへの返り値
    print(outputImage)