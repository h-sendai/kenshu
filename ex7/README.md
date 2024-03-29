# ヒストグラム図、グラフ図の作成

## 実習環境の確認

今回の研修環境では、研修用PCの各自のホームディレクトリにある
public_htmlディレクトリにファイルをおくと、Webブラウザで
``http://kenshu00.kek.jp/~username/`` (usernameの部分は
各自にわりあてたユーザー名にすること。例: http://kenshu00.kek.jp/~guest99/)
(``~``を入力できない場合は``%7e``で代用できる。例: http://kenshu00.kek.jp/%7eguest99)
でファイル一覧を見ることができるのでここでグラフファイル、
ヒストグラムファイルを作る。

```
cd
cd public_html
echo hello > hello.txt
```
として``hello.txt``を作り、Webブラウザでアクセスして
``hello``と表示されるかどうか確認してください。

## ツールあれこれ

ex6ではヒストグラムデータを自分で作ってみたが、
実際にはこのあと図を書くことが多い。いろいろツールはある:

- gnuplot (古来からあるツール。グラフ、ヒストグラム図を作る。ヒストグラムデータを作る機能はない)
- ROOT (https://root.cern/ 素粒子原子核分野ではこれを使うことが多い。ヒストグラムデータを作る機能と
図にする機能がある(その他いろいろできる))
- matplotlib (pythonを使っている)

ここではgnuplotとROOTを使ってみる。

## gnuplot

### セットアップ

- AlmaLinux 8: dnf install gnuplot
- AlmaLinux 9: dnf instal epel; dnf install gnuplot
- MacOS: homebrewをセットしてbrew install gnuplot
- Windows: よくしらないので検索してみてください

### グラフの作り方

```
% cd
% cd public_html
% gnuplot
	G N U P L O T
	Version 5.4 patchlevel 8    last modified 2023-06-01

	Copyright (C) 1986-1993, 1998, 2004, 2007-2023
	Thomas Williams, Colin Kelley and many others

	gnuplot home:     http://www.gnuplot.info
	faq, bugs, etc:   type "help FAQ"
	immediate help:   type "help"  (plot window: hit 'h')

Terminal type is now 'qt'
gnuplot> set term pngcairo size 800,400
Terminal type is now 'pngcairo'
Options are ' background "#ffffff" enhanced fontscale 1.0 size 800, 400 '
gnuplot> set output 'gnuplot-sin.png'
gnuplot> plot [0:2*pi] sin(x)
gnuplot> quit
```
とすると``gnuplot-sin.png``というファイルができるのでWebブラウザで見てみる。

(解説)

```
gnuplot> set term pngcairo size 800,400
```

- ``gnuplot>``はgnuplotが表示したプロンプト(入力しない)。
``term pngcairo``を指定するとpngファイルを作成する。
``size 800,400``は生成するpngファイルの横縦のピクセル数。

```
gnuplot> set output 'gnuplot-sin.png'
```

- ``gnuplot-sin.png``というファイル名を指定

```
gnuplot> plot [0:2*pi] sin(x)
```

- ``[0:2*pi]`` x軸範囲を指定。gnuplotでは``pi``でpiの値を指定できる。

(注) xが0に近いときsin(x)はxで近似できるので手で書くときはそれを
意識するときれいに書ける。pi/2付近もそんなにまるまっていないのに注意。
