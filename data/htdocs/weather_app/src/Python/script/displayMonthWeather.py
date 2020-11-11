from scipy import interpolate
import os, sys, const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# コマンドライン引数取得
args= sys.argv
file = args[1] + ".csv"
month = int(args[2])
variable = args[3]
runningMeanPeriod = int(args[4])
num = int(args[5])

# 値取得
data =  pd.read_csv(const.DATA_PATH_WEATHER + file, header=0, encoding='cp932')
values = data[data['Month'] == month]
# 欠測値を置換
values = values.replace(-999.0, None)

# 移動平均取得
if(runningMeanPeriod != 0):
    # 欠測値がある場合、線形補完する
    noMissingValue = values[variable].interpolate(kind='liner')
    runningMeanValue = noMissingValue.rolling(window = runningMeanPeriod, center = True).mean()

# 作図
fig = plt.figure(dpi=100, figsize=(7,3))
plt.plot(values['Year'], values[variable], color="black", linewidth=0.7, linestyle="-", label="")

if(runningMeanPeriod != 0):
    plt.plot(values['Year'], runningMeanValue, color="blue", linewidth=1.5, linestyle="-", label="移動平均")

plt.xlabel("Year", fontsize=14, fontname='Times New Roman') # x軸のタイトル
plt.grid()
plt.subplots_adjust(left=0.1, right=0.98, bottom=0.15, top=0.98)


outputImage = const.TMP_IMG1
if (num != 1):
  outputImage = const.TMP_IMG2
imagePath = const.IMG_PATH + outputImage
fig.savefig(imagePath)

# cakephp側への出力用
print(outputImage)