import csv

"""
 csv→マークダウン形式の表における行 に変換
 input：list.csv
 output：output.txt
 実行コマンド：python output.py
 出力書式：| index(1~) | [テキスト](リンク) |
"""
def main():
    OUTPUT_PATH = './data/'
    DATA_FILE = OUTPUT_PATH + 'list.csv'
    OUTPUT_FILE = OUTPUT_PATH + 'output.txt'
    output_list = []

    # csvファイル読み取り
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)

        for index, line in enumerate(reader):
            s = f'| {str(index+1)} | [{line[0]}]({line[1]}) |\n'
            output_list.append(s)

    # txtファイルへ出力
    with open(OUTPUT_FILE, 'w') as f2:
        for line in output_list:
            f2.write(line)

if __name__ == "__main__":
  main()
