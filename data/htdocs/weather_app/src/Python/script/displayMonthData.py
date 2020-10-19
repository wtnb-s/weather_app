import os, sys, const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = sys.argv[1] + ".csv"
data =  pd.read_csv(const.DATA_TEMP_PATH + file, header=None, encoding='cp932').values.tolist()
values = [x[0:3] for x in data if x[1] == 10]
value = {}
# 気温データ取得
value['temp'] = [x[2] for x in values]
# 年データ取得
value['time'] = [x[0] for x in values]

fig = plt.figure()
plt.plot(value['time'], value['temp'], color="blue", linewidth=1, linestyle="-")
plt.grid()

imagePath = const.IMG_PATH + const.TMP_IMG
fig.savefig(imagePath)
# cakephp側への出力用
print(const.TMP_IMG)