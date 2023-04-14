#!/usr/bin/env python3

import sys

# ビン数 5の例
# 各ビンの値は下端は含め、上端は含めないのが普通(?)
# [ bin_min, bin_max)
#
#        |-----|-----|-----|-----|-----|
#      x_min                         x_max
# ビン番号  0     1     2     3     4
# データ値をxとすると
# (x - x_min)/ビン幅の整数部分がビン番号になる

def usage():
    msg = 'Usage: histogram x_min x_max n_bin data'
    sys.stderr.write(msg + '\n')

def main():
    if len(sys.argv) != 5:
        usage()
        sys.exit(1)

    x_min     = float(sys.argv[1])
    x_max     = float(sys.argv[2])
    n_bin     = int(sys.argv[3])
    data_file = sys.argv[4]

    count = list()
    underflow = 0
    overflow  = 0
    for i in range(n_bin):
        count.append(0)

    bin_width = (x_max - x_min) / n_bin
    with open(data_file, 'r') as f:
        for line in f:
            x = float(line.strip())
            if x < x_min:
                underflow += 1
                continue
            if x >= x_max:
                overflow += 1
                continue
            bin_num = int((x - x_min) / bin_width)
            count[bin_num] += 1
    
    for i in range(n_bin):
        bin_min = x_min + bin_width*i
        bin_max = x_min + bin_width*(i+1)
        print('%.3f %.3f %d' % (bin_min, bin_max, count[i]))

if __name__ == '__main__':
    main()
