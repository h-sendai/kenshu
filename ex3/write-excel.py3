#!/usr/bin/python3

import openpyxl

city = {}
city['北海道'] = '札幌市'
city['青森県'] = '青森市'
city['秋田県'] = '秋田市'
city['岩手県'] = '盛岡市'

work_book  = openpyxl.Workbook()
work_sheet = work_book.active

row = 1
for k, v in city.items():
    work_sheet.cell(row = row, column = 1).value = k
    work_sheet.cell(row = row, column = 2).value = v
    work_sheet.cell(row = row, column = 3).value = row
    work_sheet.cell(row = row, column = 4).value = str(row)
    row += 1

work_book.save('new.xlsx')
