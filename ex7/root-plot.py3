#!/usr/bin/python3

import os
import sys
import time
import random
import ROOT

def main():
    c1 = ROOT.TCanvas('c1', 'C1', 1200, 800)
    h = ROOT.TH1F('hist', 'HIST', 200, -10.0, 10.0)
    for i in range(10000):
        x = random.normalvariate(0.0, 1.0)
        h.Fill(x)
    h.Draw()
    c1.SetLogy()
    c1.Update()

    c1.Print('histo.png')

if __name__ == '__main__':
    main()
