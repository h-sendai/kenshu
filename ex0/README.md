# Pythonモジュールのセットアップ、ファイルのダウンロード

## GitHubからファイルをダウンロード

次のコマンドを実行して実習用ファイルをダウンロードする:

(注)
- ``[sendai@kenshu00 ~]$``はシェルのプロンプトで入力する必要はない。
- ``[sendai@kenshu00 ~]$``の行を入力する。
- 次の``[sendai@kenshu00 ~]$``までがコマンドの出力。


commmand:
```console
git clone https://github.com/h-sendai/kenshu.git
```

```console
[sendai@kenshu00 ~]$ git clone https://github.com/h-sendai/kenshu.git
Cloning into 'kenshu'...
remote: Enumerating objects: 255, done.
remote: Counting objects: 100% (168/168), done.
remote: Compressing objects: 100% (108/108), done.
remote: Total 255 (delta 87), reused 123 (delta 47), pack-reused 87
Receiving objects: 100% (255/255), 34.84 KiB | 6.97 MiB/s, done.
Resolving deltas: 100% (114/114), done.
[sendai@kenshu00 ~]$
```

ls コマンドでkenshuというディレクトリの中身を見てみる:

```console
[sendai@kenshu00 ~]$ ls -l kenshu
total 4
drwxrwxr-x. 2 sendai sendai  23 Apr  6 09:46 ex0
drwxrwxr-x. 2 sendai sendai  40 Apr  6 09:46 ex1
drwxrwxr-x. 2 sendai sendai  99 Apr  6 09:46 ex2
drwxrwxr-x. 2 sendai sendai  68 Apr  6 09:46 ex3
drwxrwxr-x. 2 sendai sendai  38 Apr  6 09:46 ex4
drwxrwxr-x. 2 sendai sendai  45 Apr  6 09:46 ex5
drwxrwxr-x. 2 sendai sendai  45 Apr  6 09:46 ex6
drwxrwxr-x. 2 sendai sendai  45 Apr  6 09:46 ex7
drwxrwxr-x. 2 sendai sendai  45 Apr  6 09:46 ex8
drwxrwxr-x. 2 sendai sendai  45 Apr  6 09:46 ex9
drwxrwxr-x. 2 sendai sendai  39 Apr  6 09:46 function
drwxrwxr-x. 2 sendai sendai  39 Apr  6 09:46 linux-command
-rw-rw-r--. 1 sendai sendai 367 Apr  6 09:46 README.md
[sendai@kenshu00 ~]$
```

<!--
get-pip.pyはpython 3.7が最小サポートバージョンになっているので
get-pip.pyを使った最新版pip3のインストールはやめる。

## pip3コマンドのインストール

pip3を使ってpython3モジュールをインストールする。

pip3もいろいろ更新されているのでここではAlmaLinux 8付属のものは使わず
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
-->

## pip3コマンドでpythonモジュールをセットアップ

このリポジトリにあるpythonスクリプトは以下のモジュールを
使用している。requests, lxmlはCentOS Stream 8にあったので
すでに使えるようになっている。
その他のモジュールはCentOS Stream 8にはないので
追加でpip3コマンドを使ってインストールする。

- requests (これはすでに使えるようになっている)
- lxml (これもすでに使えるようになっている)
- bs4 (これもすでに使えるようになっている)
- openpyxl (これをpip3コマンドで追加する)

```console
[sendai@kenshu00 ~]$ pip3 install openpyxl --user
```

``--user``を指定するとシステム領域(/usrなど)ではなくホームディレクトリ以下に
インストールされる。今回の場合、$HOME/.local/lib/python3.6/site-packagesなどが作られ、そのなかに
モジュールファイルが入る。

これくらいなら手で打ってもOKだが、もっと大量にインストールするなら
ファイルにシェルスクリプトとしてまとめておくと別のマシンでも使える。

```bash
#!/bin/sh

# エラーがおきたらそこで終了する
set -e 

pip3 install openpyxl --user
```

正常にモジュールがセットできかたどうか確認する:

```console
[sendai@kenshu00 ~]$ python3
Python 3.6.8 (default, Mar 25 2022, 11:15:52)
[GCC 8.5.0 20210514 (Red Hat 8.5.0-10)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> import openpyxl
>>> import bs4
>>> import lxml
>>> quit() あるいはCtrl-d
[sendai@kenshu00 ~]$
```

すでにインストールしたモジュール一覧を取得する:

```console
[sendai@kenshu00 ~]$ pip3 list
OS付属パッケージでセットされたモジュールも表示される
```

ホームディレクトリ以下にインストールしたモジュール一覧を取得する:

```console
[sendai@kenshu00 ~]$ pip3 list --user
DEPRECATION: The default format will switch to columns in the future. 
You can use --format=(legacy|columns) (or define a format=(legacy|columns)
in your pip.conf under the [list] section) to disable this warning.
et-xmlfile (1.1.0)
openpyxl (3.1.2)
```

