#!/usr/local/bin/python3

# 東海村本日の最高気温、最低気温
# https://tenki.jp/ からhtmlファイルを取得して
# 気温の部分を抜き出す。
# 最高気温、最低気温の順に出力する

import requests
import bs4

# htmlファイルの取得
r = requests.get('https://tenki.jp/forecast/3/11/4010/8341/')

# BeautifulSoup4でhtmlを解析
# 解析にはlxmlを使う
soup = bs4.BeautifulSoup(r.content, 'lxml')

# 最高気温、最低気温の取り出し

today = soup.find('section', class_ = 'today-weather')
today_high_temp = today.find('dd', class_ = 'high-temp temp').find('span', class_ = 'value').getText()
today_low_temp  = today.find('dd', class_ = 'low-temp temp').find('span', class_ = 'value').getText()

print(today_high_temp, today_low_temp)
