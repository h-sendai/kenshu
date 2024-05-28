#!/usr/bin/python3

import sys
import random
import ROOT

# Usage: ./root-plot.py3 x_min x_max n_bin data_filename
def main():
    if len(sys.argv) != 7:
        print('Usage: ./root-plot.py3 x_min x_max n_bin x_title y_title data_filename')
        sys.exit(1)

    x_min          = float(sys.argv[1])
    x_max          = float(sys.argv[2])
    n_bin          = int(sys.argv[3])
    x_title        = sys.argv[4]       
    y_title        = sys.argv[5]       
    data_filename  = sys.argv[6]

    # ROOT Canvasの作成。ここでは1200x800ピクセルを指定している。
    c1 = ROOT.TCanvas('c1', 'C1', 1200, 800)

    # ヒストグラムの作成。T: Tree (rootの根幹データ構造), H: Histogram, 1: 1次元ヒストグラム, D: データはdoubleとして扱う
    h = ROOT.TH1D('hist', 'HIST', n_bin, x_min, x_max)

    # ヒストグラムができたのでファイルを読んで、インクリメントする。
    with open(data_filename, 'r') as f:
        for line in f:
            x = float(line.strip())
            h.Fill(x)

    # ヒストグラムを描画する。
    h.GetXaxis().SetTitle(x_title)
    h.GetYaxis().SetTitle(y_title)
    h.Draw()

    # Canvasのアップデート
    c1.Update()

    # data_filename + '.png'というファイル名で画像ファイルを作る。
    image_filename = data_filename + '.png'
    c1.Print(image_filename)

if __name__ == '__main__':
    main()
