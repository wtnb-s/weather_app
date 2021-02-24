import requests, time, csv, const, pandas
from bs4 import BeautifulSoup

base_url = "http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s1.php?prec_no=%s&block_no=%s&year=%s&month=&day=1&view=p1"

def main():
  # アメダス地点情報ファイル読み込み
  amedasPlaceList = pandas.read_csv(const.DATA_PATH_PLACE, header=0)

  for place in amedasPlaceList['placeName']:
    print(place)
    #最終的にデータを集めるリスト
    AllList = [['Year', 'Month', 'LLP', 'SLP', 'Precip', 'Temp', 'MaxTemp', 'MinTemp', 'Humidity', 'Wind', 'Daylight', 'Snowfall']]
    index = amedasPlaceList['placeName'].index(place)

    for year in range(1900,2021):
      print(year)
      #2つの都市コードと年を当てはめる。
      r = requests.get(base_url%(amedasPlaceList['precNo'][index], amedasPlaceList['blockNo'][index], year))
      r.encoding = r.apparent_encoding

      # 対象である表をスクレイピング。
      soup = BeautifulSoup(r.text, 'html.parser')
      rows = soup.findAll('tr',class_='mtx')

      # 表の最初の1~3行目はカラム情報なのでスライスする
      rows = rows[3:]

      # 1日〜最終日までの１行を網羅し取得
      for row in rows:
        data = row.findAll('td')

        #１行の中には様々なデータがあるので全部取り出す
        rowData = [] #初期化
        rowData.append(str(year))
        rowData.append(str(data[0].string))
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
        AllList.append(rowData)
      time.sleep(3.0)

    #都市ごとにデータをファイルを新しく生成して書き出す
    with open(const.DATA_PATH_WEATHER + place + '.csv', 'w') as file:
      writer = csv.writer(file, lineterminator='\n')
      writer.writerows(AllList)

#取ったデータをfloat型に変換、欠測値の処理も実施
def str2float(str):
  try:
    if (str == '--'):
      return 0.0
    else:
      return float(str)
  except:
    return -999.0

if __name__ == "__main__":
    main()