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
