import os, sys, const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# コマンドライン引数取得
args= sys.argv
file = args[1] + ".csv"
month = args[2]
runningMeanPeriod = int(args[3])

# 値取得
data =  pd.read_csv(const.DATA_PATH_INDEX + file, header=0, index_col=0, encoding='cp932')
values = data[month]

print(values)

# 移動平均取得
if(runningMeanPeriod != 0):
    runningMeanValue = values.rolling(window = runningMeanPeriod, center = True).mean()

# # 作図
fig = plt.figure()
plt.plot(values, color="blue", linewidth=1, linestyle="-")
if(runningMeanPeriod != 0):
    plt.plot(runningMeanValue, color="red", linewidth=1.5, linestyle="-")
plt.grid()
plt.subplots_adjust(left=0.08, right=0.97, bottom=0.05, top=0.97)
imagePath = const.IMG_PATH + const.TMP_IMG
fig.savefig(imagePath)

# # cakephp側への出力用
# print(const.TMP_IMG)