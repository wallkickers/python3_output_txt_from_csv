import csv

"""
 list.csvからデータを読み取り、output.txtへ出力する。
 実行コマンド：python output.py
 出力書式：| index(1~) | [テキスト](リンク) |
"""
def main():
    data_file = 'list.csv'
    output_file = 'output.txt'
    output_list = []

    # csvファイル読み取り
    with open(data_file, 'r') as f:
        reader = csv.reader(f)

        for index, line in enumerate(reader):
            s = f'| {str(index+1)} | [{line[0]}]({line[1]}) |\n'
            output_list.append(s)

    # txtファイルへ出力
    with open(output_file, 'w') as f2:
        for line in output_list:
            f2.write(line)

if __name__ == "__main__":
  main()
