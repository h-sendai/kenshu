# 点検簿を作る

1日1回、なにかを点検して丸印を書く点検簿をつくる。

- 作るファイルはエクセルファイル
- A列にYYYY-MM-DD と曜日
- 土日、祝日は点検しなくてよいことにするので備考的欄を作って
祝日なら祝日名をいれる

Google geminiに作ってもらった。
指令は

```
pythonプログラム 出力ファイルはエクセルファイル A列に2026-04-01から始まる日付と曜日 B列に祝日なら祝日名をいれる
```

以下geminiの出力結果

2026年4月1日からの日付、曜日、および日本の祝日名を含むエクセルファイル（holiday_calendar_2026.xlsx）を作成するPythonプログラムです。
このプログラムの実行には、pandas（データ処理）、openpyxl（エクセル出力）、jpholiday（祝日判定）のライブラリが必要です。

必要ライブラリのインストール
ターミナルまたはコマンドプロンプトで以下を実行してください。
bash
```
pip install pandas openpyxl jpholiday
```

Pythonプログラム
python

```
import pandas as pd
import jpholiday
import datetime

def create_holiday_excel(start_date_str, end_date_str, output_file):
    # 1. 指定期間の日付範囲を作成
    date_range = pd.date_range(start=start_date_str, end=end_date_str)
    
    data = []
    for date in date_range:
        # 日付と曜日を取得 (yyyy/mm/dd (ddd) 形式)
        date_str = date.strftime('%Y/%m/%d (%a)')
        
        # 祝日名を取得
        holiday_name = jpholiday.is_holiday_name(date)
        
        # 祝日でない場合、土日を判定して「土」「日」を入れる（オプション）
        if not holiday_name:
            if date.weekday() == 5:
                holiday_name = "土"
            elif date.weekday() == 6:
                holiday_name = "日"
            else:
                holiday_name = "" # 平日は空欄
        
        data.append([date_str, holiday_name])
    
    # 2. DataFrameを作成
    df = pd.DataFrame(data, columns=['日付・曜日', '祝日・週末'])
    
    # 3. エクセルファイルへ出力
    df.to_excel(output_file, index=False)
    print(f"ファイルを作成しました: {output_file}")

# 設定
START_DATE = '2026-04-01'
# 1年分（2027年3月末まで）作成する場合
END_DATE = '2027-03-31' 
OUTPUT_FILE = 'holiday_calendar_2026.xlsx'

# 実行
create_holiday_excel(START_DATE, END_DATE, OUTPUT_FILE)
```

プログラムの解説

1. pd.date_range: 2026-04-01から1年分の日付を自動生成します。
2. jpholiday.is_holiday_name: 日本の祝日を判定し、祝日名（昭和の日、憲法記念日など）を返します。祝日でない場合はNoneを返します。
3. 曜日と土日判定: date.strftime('%Y/%m/%d (%a)') で曜日を付記しています。また、祝日でない場合に土曜日と日曜日に「土」「日」を自動で入れる処理を追加しています。
4. to_excel: pandasの機能でエクセルファイルとして保存します

geminiの出力結果ここまで。

曜日が英語(3文字形式)になっているので手動で日本語(日、月、火、...、土)に変更する。
変更点:
```console
% diff -u prog.py3 prog-ja.py3
--- prog.py3	2026-02-10 13:23:26.689624115 +0900
+++ prog-ja.py3	2026-02-10 13:24:35.306406928 +0900
@@ -2,7 +2,13 @@
 import jpholiday
 import datetime
 
+# 曜日を日本語で表示するために追加（千代）
+import locale
+
 def create_holiday_excel(start_date_str, end_date_str, output_file):
+    # 曜日を日本語で表示するために追加（千代）
+    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
+
     # 1. 指定期間の日付範囲を作成
     date_range = pd.date_range(start=start_date_str, end=end_date_str)
```

[変更後のプログラム全体](prog-ja.py3)





