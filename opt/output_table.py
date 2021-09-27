import csv

"""
  csvファイルの1行目をヘッダー,　以降の行を内容として出力する。
  input：list.csv
  output：output.txt
  command：python output_table.py
  出力書式：
  header1,header2,header3,header4...
  item1,item2,item3,item4...
  ↓
  | ヘッダー1 | ヘッダー2 | ヘッダー3 |...
  | ------------- | ------------- | ------------- |...
  | 内容1 | 内容2 | 内容3 |...
"""
def main():
    OUTPUT_PATH = './data/'
    DATA_FILE = OUTPUT_PATH + 'list.csv'
    OUTPUT_FILE = OUTPUT_PATH + 'output.txt'
    output_list = []
    item_count = 0

    # csvファイル読み取り
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)

        for column, line in enumerate(reader):
            # ヘッダー
            if column == 0:
                item_count = len(line)
                s = '|'
                for index in range(item_count):
                    # マークダウン表示のため
                    line[index] = line[index].replace('\n', '<br>')
                    line[index] = line[index].replace('-', 'ー')
                    s = s + f' {line[index]} |'
                s = s + '\n'
                output_list.append(s)

                s = '|'
                for header_item in line:
                    s = s + ' ------------- |'
                s = s + '\n'
                output_list.append(s)
            # 表
            else:
                s = '|'
                for index in range(item_count):
                    # マークダウン表示のため
                    line[index] = line[index].replace('\n', '<br>')
                    line[index] = line[index].replace('-', 'ー')
                    s = s + f' {line[index]} |'
                s = s + '\n'
                output_list.append(s)

    # txtファイルへ出力
    with open(OUTPUT_FILE, 'w') as f2:
        for line in output_list:
            f2.write(line)

if __name__ == "__main__":
  main()
