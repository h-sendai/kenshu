#!/usr/bin/python3

import subprocess

# subprocess.run(['date', '-u'])
# これは単に``date -u``コマンドを実行するだけ。
# pythonスクリプト内で出力をとりたい場合は次のようにする。

output = subprocess.run(['date', '-u'], capture_output = True)
print(output.stdout.decode().strip())
