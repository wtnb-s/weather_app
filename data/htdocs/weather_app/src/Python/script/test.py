import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "osaka.csv"
path = "../data/temp/%s" %(file)
data =  pd.read_csv(path, header=None, encoding='cp932')

time = list(data.iloc[:,0])
value = list(data.iloc[:,2])

tempSum = np.array([0] * 36)
time = np.array([0] * 36)

count = 0
for val in value:
  tempSum[count] += val
  time[count] += 1 
  if count == 35:
    count = 0
  else:
    count = count + 1

tempAve = tempSum / time
listTime = list(range(1, 37))

# 画像のプロット先の準備
fig = plt.figure()
plt.plot(listTime, tempAve, color="blue", linewidth=1, linestyle="-")

# グリッドを表示する
plt.grid()

# グラフをファイルに保存する
fig.savefig("../image/osaka.png")