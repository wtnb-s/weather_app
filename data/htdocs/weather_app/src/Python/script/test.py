import os, sys, const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = sys.argv[1] + ".csv"
month = int(sys.argv[2])

data =  pd.read_csv(const.DATA_TEMP_PATH + file, header=0, encoding='cp932')
values = data[data['mon'] == month]

runningMean = values['value'].rolling(window = 5, center = True).mean()

fig = plt.figure()
plt.plot(values['year'], values['value'], color="blue", linewidth=1, linestyle="-")
plt.plot(values['year'], runningMean, color="red", linewidth=1, linestyle="-")
plt.grid()

imagePath = const.IMG_PATH + const.TMP_IMG
fig.savefig(imagePath)
# # cakephp側への出力用
print(const.TMP_IMG)