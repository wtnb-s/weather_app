from scipy import interpolate
from codes import const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getDailyRange(values):
    return values['MaxTemp'] - values['MinTemp']

def main(city: str, month: int, variable: str, runningMeanPeriod :int = 0):    
    # 値取得
    file =  city + ".csv"
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
    plt.xlabel("Year", fontsize=14)
    plt.grid()
    plt.subplots_adjust(left=0.1, right=1.0, bottom=0.15, top=1.0)
    
    # 画像出力
    outputImage = const.TMP_IMG
    imagePath = const.IMG_PATH + outputImage
    plt.savefig(imagePath, format="png", dpi=100, bbox_inches='tight', pad_inches=0)
    return True