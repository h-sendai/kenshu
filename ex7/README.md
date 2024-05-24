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

- gnuplot (http://gnuplot.info/ 古来からあるツール。グラフ、ヒストグラム図を作る。ヒストグラムデータを作る機能はない)
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
	Version 5.4 patchlevel 3    last modified 2021-12-24 

	Copyright (C) 1986-1993, 1998, 2004, 2007-2021
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

### gnuplotでデータをプロット

データプロットの例として
つくば市の最高気温、平均気温、最低気温を
気象庁からダウンロードしたデータ``tsukuba-kion.txt``を
置いたのでプロットしてみる。

プロットするプログラムは
[plot-tsukuba-kion](plot-tsukuba-kion)として置いてある。

```console
./plot-tsukuba-kion
```
とすると、``tsukuba-kion.png``という画像ファイルができるので

```console
cp tsukuba-kion.png ~/public_html
```

でコピーしてウェブブラウザで
http://kenshu00.kek.jp/~guestNN/
でアクセスして見てみる(NNは各自の番号を代入する)。

## ROOTでヒストグラム図を書く

ROOT (https://root.cern/) は素粒子原子核関連でよく使われている解析ツール。

### AlmaLinux 9でのセットアップ

AlmaLinux用のROOTのパッケージはFedora Projectが運営している
Extra Packages for Enterprise Linux (EPEL)リポジトリにある。
セットアップするには

```
dnf install epel-release
dnf update epel-release
dnf install root
pythonを使ってプロットするなら
dnf install python3-root
```

とする。実習用マシンにはすでに入っている。

### 使い方

``root``と入力すると
```console
% root
   ------------------------------------------------------------------
  | Welcome to ROOT 6.30/06                        https://root.cern |
  | (c) 1995-2024, The ROOT Team; conception: R. Brun, F. Rademakers |
  | Built for linuxx8664gcc on Apr 25 2024, 00:00:00                 |
  | From heads/master@tags/v6-30-06                                  |
  | With g++ (GCC) 11.4.1 20230605 (Red Hat 11.4.1-2)                |
  | Try '.help'/'.?', '.demo', '.license', '.credits', '.quit'/'.q'  |
   ------------------------------------------------------------------
root [0]

```
となりコマンド入力待ちになる。ここではこれは使わず
pythonを使ってプロットさせてみる。

プログラムは[root-plot.py3](root-plot.py3)にある。

```
./root-plot.py3
```

とすると``histo.png``という画像ファイルができるので

```
cp histo.png ~/public_html
```

でコピーして http://kenshu00.kek.jp/~guestNN/ （NNは各自の番号）
で見てみる。
