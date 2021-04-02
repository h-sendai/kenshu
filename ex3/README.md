## ex2: Excelファイルの読み書き

Pythonプログラムを書いて、Excelファイルの読み書きを行う。
書くプログラムと読むプログラムの2個のプログラムを書く。
読むほうはExcelファイルがないと読めないので書く方から作る。

## 準備

ここではopenpyxlモジュールを使ってExcelファイルの読み書きを
行う。openpyxlモジュールはPython標準ライブラリには入っていないので
まずpip3コマンドを使ってopenpyxlモジュールのセットアップを
行う。
セットが終わったら、python3ラインインタプリタを使って使えるか
どうか試してみる。
プロンプト(>>>)でimport openpyxlと入力し、次のプロンプトがでれば
使えるようになっている。

    $ pip3 install openpyxl --user
    $ python3
    Python 3.7.3 (default, Apr 10 2019, 12:54:05)
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import openpyxl
    >>> (ここで入力待ちになれば正常)

次のようになるときはなにかおかしい:

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'openpyxlx'
    >>>

## excelファイルを作る

write-excel.py3を読んでみてどんなファイルができるか考える。
実行してみる:

    ./write-excel.py3

newfile.xlsxというファイルができていると思うのでそれを
共有フォルダにコピーする。

    cp newfile.xlsx /media/sf_vboxsf/
    
ホスト環境側で、共有フォルダに指定したフォルダに移動し、
newfile.xlsxをエクセルで開いて、エクセルで読めるxlsx
ファイルであることを確認する。

## excelファイルを読む

read-excel.py3を実行して、pythonでもエクセルファイルが読める
ことを確認する:

    ./read-excel.py3

## 余談

xlsxファイルは普通にzipファイルなのでlinux上でunzipコマンドを
使って中身を取り出すことができる:

    unzip -l fileでzipファイル内の一覧をとれる
    bash$ unzip -l new.xlsx
    Archive:  new.xlsx
      Length      Date    Time    Name
    ---------  ---------- -----   ----
          177  06-19-2019 14:22   docProps/app.xml
          555  06-19-2019 14:22   docProps/core.xml
        10140  06-19-2019 14:22   xl/theme/theme1.xml
         1364  06-19-2019 14:22   xl/worksheets/sheet1.xml
          838  06-19-2019 14:22   xl/styles.xml
          531  06-19-2019 14:22   _rels/.rels
          546  06-19-2019 14:22   xl/workbook.xml
          504  06-19-2019 14:22   xl/_rels/workbook.xml.rels
          975  06-19-2019 14:22   [Content_Types].xml
    ---------                     -------
        15630                     9 files
