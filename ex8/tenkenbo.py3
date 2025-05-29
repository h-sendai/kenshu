#!/usr/bin/python3

import os
import sys
import time
import datetime
import calendar
import jpholiday
from string import Template
import subprocess

# Usage
# ./this program month year
# if year is not specified, this year will be substituted.
# if month is noit specified, this month will be substituted.

dow = [ '月' , '火' , '水' , '木' , '金' , '土' , '日' ]

tpl = r'''
\documentclass[11pt]{jsarticle}
\thispagestyle{empty}
\usepackage{array}

\author{}
\date{}
\title{}

\begin{document}
\begin{center}自主点検記録（日常）（${year}年${month}月）担当区域: 第3研究棟205-209 \end{center}
\begin{center}
\begin{tabular}{|r|wc{1.5cm}|wc{1.5cm}|wc{1.5cm}|p{5cm}|} \hline
日（曜日）&  ポット & 消灯 & 点検者 & 備考\\ \hline
${days}
\end{tabular}
\end{center}
\end{document}
'''

def main():
    year = 0
    month = 0
    if len(sys.argv) == 3:
        month = int(sys.argv[1])
        year  = int(sys.argv[2])
    if len(sys.argv) == 2:
        month = int(sys.argv[1])
        year  = datetime.date.today().year
    elif len(sys.argv) == 1:
        month = datetime.date.today().month
        year  = datetime.date.today().year

    if not 1 <= month <= 12:
        print('range error: month %d' % month)
        sys.exit(1)
        
    last_day = calendar.monthrange(year, month)[1]
    days = ''
    for day in range(1, last_day + 1):
        dt =  datetime.date(year, month, day)
        dow_index = dt.weekday()
        days += '%02d（%s）& & & &' % (day, dow[dow_index])
        holiday_name = jpholiday.is_holiday_name(dt)
        if holiday_name:
            days += holiday_name
        days += ' \\\\ \\hline\n'

    t = Template(tpl)
    o = t.substitute(year = str(year), month = str(month), days = days)
    filename_base = 'tenkenbo.%02d-%02d' % (year, month)
    filename_tex  = filename_base +  '.tex'
    f = open(filename_tex, 'w')
    f.writelines(o)
    f.close()

    subprocess.run(['platex',   filename_base])
    subprocess.run(['dvipdfmx', filename_base])
    subprocess.run(['rm', '-f', filename_base + '.aux'])
    subprocess.run(['rm', '-f', filename_base + '.dvi'])
    subprocess.run(['rm', '-f', filename_base + '.log'])


if __name__ == '__main__':
    main()
