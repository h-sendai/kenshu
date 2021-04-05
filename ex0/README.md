# Pythonモジュールのセットアップ

## pip3コマンドのインストール

pip3を使ってpython3モジュールをインストールする。

pip3もいろいろ更新されているのでここではCentOS 7付属のものは使わず
最新版をダウンロードして使うことにする。

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

とするとhttps://bootstrap.pypa.io/get-pip.pyからgetpip.pyをダウンロードし、
get-pip.pyというファイルに保存する。ダウンロード後これを走らせる:

```
python3 get-pip.py --user
```

``--user``を指定するとシステム領域(/usrなど)ではなくホームディレクトリ以下に
インストールされる。今回の場合、$HOME/.local/binなどが作られ、そのなかにpip3コマンドが入る。
bashを使っているならPATHに$HOME/.local/binが入っているのでそのままでpip3コマンドが
走る。

どのpip3が実行されるかは``which pip3``、あるいは``which -a pip3``とするとわかる:

```
% which -a pip3
~/.local/bin/pip3
/usr/bin/pip3
```

## pip3コマンドでpythonモジュールをセットアップ

続けて以下のpythonモジュールをインストールする:

- requests
- openpyxl
- bs4
- lxml

```
% pip3 install requests
% pip3 install openpyxl
% pip3 install bs4
% pip3 install lxml
```

これくらいなら手で打ってもOKだが、もっと大量にインストールするなら
ファイルにシェルスクリプトとしてまとめておくと別のマシンでも使える。

```
#!/bin/sh

# エラーがおきたらそこで終了する
set -e 

pip3 install requests
pip3 install openpyxl
pip3 install bs4
pip3 install lxml
```

正常にモジュールがセットできかたどうか確認する:

```
[sendai@localhost ~]$ python3
Python 3.6.8 (default, Nov 16 2020, 16:55:22)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> import openpyxl
>>> import bs4
>>> import lxml
>>> quit() あるいはCtrl-d
[sendai@localhost ~]$
```

