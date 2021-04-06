# Pythonモジュールのセットアップ

## pip3コマンドのインストール

pip3を使ってpython3モジュールをインストールする。

pip3もいろいろ更新されているのでここではCentOS 7付属のものは使わず
最新版をダウンロードして使うことにする。

```console
[sendai@kenshu00 ~]$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1882k  100 1882k    0     0  7674k      0 --:--:-- --:--:-- --:--:-- 7714k
[sendai@kenshu00 ~]$
```

とすると``https://bootstrap.pypa.io/get-pip.py``から``getpip.py``をダウンロードし、
``get-pip.py``というファイルに保存する。ダウンロード後これを走らせる:

```console
[sendai@kenshu00 ~]$ python3 get-pip.py --user
Collecting pip
  Using cached pip-21.0.1-py3-none-any.whl (1.5 MB)
Collecting wheel
  Using cached wheel-0.36.2-py2.py3-none-any.whl (35 kB)
Installing collected packages: wheel, pip
Successfully installed pip-21.0.1 wheel-0.36.2
[sendai@kenshu00 ~]$
```

``--user``を指定するとシステム領域(/usrなど)ではなくホームディレクトリ以下に
インストールされる。今回の場合、$HOME/.local/binなどが作られ、そのなかにpip3コマンドが入る。
bashを使っているならPATHに$HOME/.local/binが入っているのでそのままでpip3コマンドが
走る。bashではなく他のシェルを使っている場合はPATHに追加するか
$HOME/binからシンボリックリンクをはって対処する。

どのpip3が実行されるかは``which pip3``、あるいは``which -a pip3``とするとわかる:

```console
[sendai@kenshu00 ~]$ which -a pip3
~/.local/bin/pip3
/usr/bin/pip3
[sendai@kenshu00 ~]$
```

## pip3コマンドでpythonモジュールをセットアップ

続けて以下のpythonモジュールをインストールする:

- requests
- openpyxl
- bs4
- lxml

```console
[sendai@kenshu00 ~]$ pip3 install requests --user
Collecting requests
  Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)
Collecting idna<3,>=2.5
  Using cached idna-2.10-py2.py3-none-any.whl (58 kB)
Collecting chardet<5,>=3.0.2
  Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
Installing collected packages: urllib3, idna, chardet, certifi, requests
Successfully installed certifi-2020.12.5 chardet-4.0.0 idna-2.10 requests-2.25.1 urllib3-1.26.4
[sendai@kenshu00 ~]$ # 以下コマンドのみのせています
[sendai@kenshu00 ~]$ pip3 install openpyxl --user
[sendai@kenshu00 ~]$ pip3 install bs4      --user
[sendai@kenshu00 ~]$ pip3 install lxml     --user
```

これくらいなら手で打ってもOKだが、もっと大量にインストールするなら
ファイルにシェルスクリプトとしてまとめておくと別のマシンでも使える。

```bash
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
[sendai@kenshu00 ~]$ python3
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

