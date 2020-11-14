import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os, sys, const

# ファイル読み込み
df = gpd.read_file('/root/weather_app/src/Python/data/map/japan-mi.geojson')
locations = pd.read_csv("/root/weather_app/src/Python/data/city/city.csv", header=0)

plt.figure()
# 地図表示
with plt.style.context("ggplot"):
  df.plot(figsize=(8, 8), edgecolor='#444', facecolor='white', linewidth = 0.7);
  plt.xlim([126,150])
  plt.ylim([25.5,46])

# プロット
plt.scatter(locations['lon'], locations['lat'], marker='o', s=10, color="red", alpha=0.8, linewidths = 1)

# 画像出力
outputImage = const.TMP_IMG
imagePath = const.IMG_PATH + outputImage
plt.savefig(imagePath, format="png", dpi=300, bbox_inches='tight', pad_inches=0)