place_codeA = [14, 21, 23, 31, 32, 33, 35, 34, 36, 54, 56, 55, 48, 41, 57, 42, 43, 40, 52, 51, 49, 45, 53, 50, 46, 68, 69, 61, 60, 67, 66, 63, 65, 64, 73, 72, 74, 71, 81, 82, 85, 83, 84, 86, 88, 87]
place_codeB = [47412, 47423, 47430, 47575, 47582, 47584, 47588, 47590, 47595, 47604, 47605, 47607, 47610, 47615, 47616, 47624, 47626, 47629, 47632, 47636, 47638, 47648, 47651, 47656, 47670, 47741, 47746, 47759, 47761, 47765, 47768, 47770, 47777, 47780, 47887, 47891, 47893, 47895, 47762, 47807, 47813, 47815, 47817, 47819, 47827, 47830]
place_name = ["札幌", "室蘭", "函館", "青森", "秋田", "盛岡", "山形", "仙台", "福島", "新潟", "金沢", "富山", "長野", "宇都宮", "福井", "前橋", "熊谷", "水戸", "岐阜", "名古屋", "甲府", "銚子", "津", "静岡", "横浜", "松江", "鳥取", "京都", "彦根", "広島", "岡山", "神戸", "和歌山", "奈良", "松山", "高松", "高知", "徳島", "下関", "福岡", "佐賀", "大分", "長崎", "熊本", "鹿児島", "宮崎"]   

import requests
from bs4 import BeautifulSoup
import csv, const

base_url = "http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s1.php?prec_no=%s&block_no=%s&year=%s&month=&day=1&view=p1"
output_path = const.DATA_PATH_TEMP

#取ったデータをfloat型に変えるやつ。(データが取れなかったとき気象庁は"/"を埋め込んでいるから0に変える)
def str2float(str):
  try:
    return float(str)
  except:
    return 0.0


if __name__ == "__main__":
  for place in place_name:
    print(place)
    #最終的にデータを集めるリスト
    All_list = [['年月日', '陸の平均気圧(hPa)', '海の平均気圧(hPa)', '降水量(mm)', '平均気温(℃)', '最高気温(℃)', '最低気温(℃)', '平均湿度(%)', '平均風速(m/s)', '日照時間(h)', '降雪(cm)']]
    index = place_name.index(place)

    for year in range(2007,2008):
      print(year)
      #2つの都市コードと年を当てはめる。
      r = requests.get(base_url%(place_codeA[index], place_codeB[index], year))
      r.encoding = r.apparent_encoding

      # 対象である表をスクレイピング。
      soup = BeautifulSoup(r.text)
      rows = soup.findAll('tr',class_='mtx')

      # 表の最初の1~3行目はカラム情報なのでスライスする
      rows = rows[3:]

      # 1日〜最終日までの１行を網羅し取得
      for row in rows:
        data = row.findAll('td')

        #１行の中には様々なデータがあるので全部取り出す
        rowData = [] #初期化
        rowData.append(str(year) + "/" + str(data[0].string))
        rowData.append(str2float(data[1].string))
        rowData.append(str2float(data[2].string))
        rowData.append(str2float(data[3].string))
        rowData.append(str2float(data[7].string))
        rowData.append(str2float(data[8].string))
        rowData.append(str2float(data[9].string))
        rowData.append(str2float(data[12].string))
        rowData.append(str2float(data[14].string))
        rowData.append(str2float(data[19].string))
        rowData.append(str2float(data[21].string))

        #次の行にデータを追加
        All_list.append(rowData)

    #都市ごとにデータをファイルを新しく生成して書き出す
    with open(const.DATA_PATH_WEATHER + place + '.csv', 'w') as file:
      writer = csv.writer(file, lineterminator='\n')
      writer.writerows(All_list)
