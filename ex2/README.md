## ファイルを読む

ファイルを読むのは基本なので一度実行してみる。

``sample0.txt``、``sample1.txt``とふたつのテスト用ファイルを
用意してある:

```console
[sendai@kenshu00 ex2]$ cat sample0.txt
1
2
3
4
5
[sendai@kenshu00 ex2]$ cat sample1.txt
10
20
30
40
50
[sendai@kenshu00 ex2]$
```

## コード中にファイル名をいれておくコード

[その0 (read-file-filename-0.py3)](read-file-filename-0.py3)

```console
[sendai@kenshu00 ex2]$ ./read-file-filename-0.py3
1

2

3

4

5

[sendai@kenshu00 ex2]$
```

lineの行末に改行コードが入っているのとprint()はデフォルトでは最後に
改行コードを出力するのがあいまって各行の後ろの空行が入っている。

空行が入らないようにするには2とおりある(もっとあるかもしれない):

- print()で改行コードを出力しないようにする(``end = ''``の追加) [(read-file-filename-1.py3)](read-file-filename-1.py3)
- lineから改行コードをとりのぞいてprint()を実行する [(read-file-filename-2.py3)](read-file-filename-2.py3)

続いてファイル名をコマンド引数で指定する方法を取り上げる。

## ファイル名を引数で指定する

### 準備

pythonスクリプトではコマンド引数はsys.argv配列に入っている。
``import sys``が必要。
``sys.argv[0]``にはシェルコマンドラインで指定したコマンドが入っている。
``sys.argv[1]``以降に引数が入る。

```python
#!/usr/bin/python3

import sys

for i in range(len(sys.argv)):
    print(i, sys.argv[i])

```

```console
[sendai@kenshu00 ex2]$ ./sys-argv.py3 file0 file1
0 ./sys-argv.py3
1 file0
2 file1
```

### 実装

実装例: [read-file.py3](read-file.py3)

実行してみたところ:

```console
[sendai@kenshu00 ex2]$ ./read-file.py3 sample0.txt
1
2
3
4
5
[sendai@kenshu00 ex2]$ ./read-file.py3 sample1.txt
10
20
30
40
50
[sendai@kenshu00 ex2]$
```

## エラーの取り扱い

存在しないファイルを指定するとエラーメッセージを出力して終了する:

```console
[sendai@kenshu00 ex2]$ ./read-file.py3 no-such-file
Traceback (most recent call last):
  File "./read-file.py3", line 7, in <module>
    with open(sys.argv[1], 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'no-such-file'
[sendai@kenshu00 ex2]$
```

## 複数ファイルの取り扱い


### catコマンド

本物のcatコマンドは複数ファイルを引数にとることができる:

```console
[sendai@kenshu00 ex2]$ cat sample0.txt sample1.txt
1
2
3
4
5
10
20
30
40
50
[sendai@kenshu00 ex2]$
```

途中に存在しないファイルが指定されてもそこで止まらない(エラーメッセージは出す):

```console
[sendai@kenshu00 ex2]$ cat sample0.txt no-such-file sample1.txt
1
2
3
4
5
cat: no-such-file: No such file or directory
10
20
30
40
50
[sendai@kenshu00 ex2]$
```

### pythonでの実装

エラーがあっても継続したければpythonではtry ... except ... で囲んでおく。

```python
#!/usr/bin/python3

import sys

def cat(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line, end = '')
    except Exception as e:
        print(e)

def main():
    for i in sys.argv[1:]:
        cat(i)

if __name__ == '__main__':
    main()
```

実行してみる:

```console
[sendai@kenshu00 ex2]$ ./mycat.py3 sample0.txt no-such-file sample1.txt
1
2
3
4
5
[Errno 2] No such file or directory: 'no-such-file'
10
20
30
40
50
[sendai@kenshu00 ex2]$
```
