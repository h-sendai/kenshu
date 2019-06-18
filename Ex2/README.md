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

    $ sudo pip3 install openpyxl
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
