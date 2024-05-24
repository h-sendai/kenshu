#!/usr/bin/python3

import random
import ROOT

def main():
    # ROOT Canvasの作成。ここでは1200x800ピクセルを指定している。
    c1 = ROOT.TCanvas('c1', 'C1', 1200, 800)

    # ヒストグラムの作成。T: Tree (rootの根幹データ構造), H: Histogram, 1: 1次元ヒストグラム, D: データはdoubleとして扱う
    h = ROOT.TH1D('hist', 'HIST', 200, -10.0, 10.0)

    # ヒストグラムができたのでそこに院クリメントするデータを生成する。
    # ここではpython randomモジュールを使って、平均0.0, 標準偏差 1.0の
    # 正規分布データを生成している。
    # h.Fill()でデータをヒストグラムに入れている。
    for i in range(10000):
        x = random.normalvariate(0.0, 1.0)
        h.Fill(x)

    # ヒストグラムを描画する。
    h.Draw()

    # そのままでもよいが例示のため縦軸をログスケールにしている。
    c1.SetLogy()

    # Canvasのアップデート
    c1.Update()

    # histo.pngというファイル名で画像ファイルを作る。
    c1.Print('histo.png')

if __name__ == '__main__':
    main()
