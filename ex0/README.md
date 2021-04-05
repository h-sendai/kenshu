# Pythonモジュールのセットアップ

## pip3コマンドのインストール

pip3を使ってpython3モジュールをインストールする。

pip3もいろいろ更新されているのでここではCentOS 7付属のものは使わず
最新版をダウンロードして使うことにする。

```console
sendai@localhost% curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

とすると``https://bootstrap.pypa.io/get-pip.py``から``getpip.py``をダウンロードし、
``get-pip.py``というファイルに保存する。ダウンロード後これを走らせる:

```console
sendai@localhost% python3 get-pip.py --user
```

``--user``を指定するとシステム領域(/usrなど)ではなくホームディレクトリ以下に
インストールされる。今回の場合、$HOME/.local/binなどが作られ、そのなかにpip3コマンドが入る。
bashを使っているならPATHに$HOME/.local/binが入っているのでそのままでpip3コマンドが
走る。bashではなく他のシェルを使っている場合はPATHに追加するか
$HOME/binからシンボリックリンクをはって対処する。

どのpip3が実行されるかは``which pip3``、あるいは``which -a pip3``とするとわかる:

```console
sendai@localhost% which -a pip3
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
% pip3 install requests --user
% pip3 install openpyxl --user
% pip3 install bs4      --user
% pip3 install lxml     --user
```

これくらいなら手で打ってもOKだが、もっと大量にインストールするなら
ファイルにシェルスクリプトとしてまとめておくと別のマシンでも使える。

```
#!/bin/sh

# エラーがおきたらそこで終了する
set -e 

pip3 install requests --user
pip3 install openpyxl --user
pip3 install bs4      --user
pip3 install lxml     --user
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

