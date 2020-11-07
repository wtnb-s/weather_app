from scipy import interpolate
import os, sys, const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# コマンドライン引数取得
args= sys.argv
file = args[1] + ".csv"
month = int(args[2])
runningMeanPeriod = int(args[3])

# 値取得
data =  pd.read_csv(const.DATA_PATH_TEMP + file, header=0, encoding='cp932')
values = data[data['mon'] == month]

# 移動平均取得
if(runningMeanPeriod != 0):
    # 欠測値がある場合、線形補完する
    noMissingValue = values['value'].interpolate(kind='liner')
    runningMeanValue = noMissingValue.rolling(window = runningMeanPeriod, center = True).mean()

# 作図
fig = plt.figure()
plt.plot(values['year'], values['value'], color="black", linewidth=0.7, linestyle="-", label="")
if(runningMeanPeriod != 0):
    plt.plot(values['year'], runningMeanValue, color="blue", linewidth=1.5, linestyle="-")

plt.xlabel("Year", fontsize=14, fontname='Times New Roman') # x軸のタイトル
plt.ylabel("Temperature(℃)", fontsize=14, fontname='Times New Roman') # y軸のタイトル
plt.grid()
plt.subplots_adjust(left=0.08, right=0.97, bottom=0.14, top=0.95)
imagePath = const.IMG_PATH + const.TMP_IMG
fig.savefig(imagePath)

# cakephp側への出力用
print(const.TMP_IMG)