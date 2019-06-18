#!/usr/local/bin/python3

from openpyxl import load_workbook

work_book  = load_workbook(filename='new.xlsx', read_only=True)
work_sheet = work_book.active

for row in work_sheet.rows:
    for cell in row:
        print(cell.value, end = ' ')
    print()
