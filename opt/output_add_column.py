import csv

"""
 list.csvからデータを読み取り、output.txtへ出力する。
 list.csvに3列目が存在する場合に列を追加する。
 実行コマンド：python output_add_column.py
 出力書式：
 　パターンA 3列目がない場合
 　| index(1~) | [テキスト](リンク) | ー |
 　パターンB 3列目がある場合
 　| index(1~) | [テキスト](リンク) | [テキスト](リンク) |
"""
def main():
    data_file = 'list.csv'
    output_file = 'output.txt'
    output_list = []

    # csvファイル読み取り
    with open(data_file, 'r') as f:
        reader = csv.reader(f)

        for index, line in enumerate(reader):
            if(line[3] == ''):
                s = f'| {str(index+1)} | [{line[0]}]({line[1]}) | ー |\n'
            else:
                s = f'| {str(index+1)} | [{line[0]}]({line[1]}) | [{line[2]}]({line[3]}) |\n'
            output_list.append(s)

    # txtファイルへ出力
    with open(output_file, 'w') as f2:
        for line in output_list:
            f2.write(line)

if __name__ == "__main__":
  main()
