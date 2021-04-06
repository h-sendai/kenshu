## ex1 環境テスト

どのプログラム言語でも最初に書くのはたいていは画面になにか
表示するというプログラム(らしい)。

hello.py3という文字列を表示するプログラムの例。
書いたあと、``python3 hello.py3``として実行するか、ファイルに実行権を付け
(``chmod +x hello.py3``)、``./hello.py3``として実行する:

```console
[sendai@kenshu00 ~]$ cd
[sendai@kenshu00 ~]$ cd kenshu/
[sendai@kenshu00 kenshu]$ cd ex1

[sendai@kenshu00 ex1]$ ls -l
total 8
-rw-rw-r--. 1 sendai sendai  35 Apr  6 14:59 hello.py3
-rw-rw-r--. 1 sendai sendai 327 Apr  6 14:59 README.md

[sendai@kenshu00 ex1]$ python3 hello.py3
hello

[sendai@kenshu00 ex1]$ chmod +x hello.py3
[sendai@kenshu00 ex1]$ ls -l hello.py3
-rwxrwxr-x. 1 sendai sendai 35 Apr  6 14:59 hello.py3

[sendai@kenshu00 ex1]$ ./hello.py3
hello
[sendai@kenshu00 ex1]$
```
