#!/usr/bin/python3

# 東海村本日、明日の予想最高最低気温を表示する。
# https://tenki.jp/ からhtmlファイルを取得して
# 気温の部分を抜き出す。
# 最高気温、最低気温の順に出力する

import requests
import bs4

# htmlファイルの取得
r = requests.get('https://tenki.jp/forecast/3/11/4010/8341/')

# BeautifulSoup4でhtmlを解析
# htmlの解析にはlxmlを使う
soup = bs4.BeautifulSoup(r.content, 'lxml')

# 最高気温、最低気温の取り出し

today = soup.find('section', class_ = 'today-weather')
today_high_temp = today.find('dd', class_ = 'high-temp temp').find('span', class_ = 'value').getText()
today_low_temp  = today.find('dd', class_ = 'low-temp temp' ).find('span', class_ = 'value').getText()

tomorrow = soup.find('section', class_ = 'tomorrow-weather')
tomorrow_high_temp = tomorrow.find('dd', class_ = 'high-temp temp').find('span', class_ = 'value').getText()
tomorrow_low_temp  = tomorrow.find('dd', class_ = 'low-temp temp' ).find('span', class_ = 'value').getText()

print('today:   ', today_high_temp, today_low_temp)
print('tomorrow:', tomorrow_high_temp, tomorrow_low_temp)
