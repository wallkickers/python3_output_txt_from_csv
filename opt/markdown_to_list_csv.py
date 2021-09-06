import csv

"""
 markdown.csvからデータを読み取り、list.csvへ出力する。
 マークダウン形式で記載したテーブルに変更を加えるために
 マークダウン→プレーンに修正したかったので作成。
 実行コマンド：python markdown_to_list_csv.py
 出力書式： | テキスト | リンク | 
"""
def main():
    data_file = 'markdown.csv'
    output_file = 'list.csv'
    output_list = []

    # csvファイル読み取り
    with open(data_file, 'r') as f:
        reader = csv.reader(f)

        # 空白削除
        reader =list(filter(None, reader))

        for index, line in enumerate(reader):
            # タイトル
            s1 = line[0].split('[')[1].split(']')[0]
            # リンクURL
            s2 = line[0].split('(')[1].split(')')[0]
            output_list.append([s1, s2])

    # csvファイルへ出力
    with open(output_file, 'w', newline='') as f2:
        for line in output_list:
            writer = csv.writer(f2)
            writer.writerow(line)

if __name__ == "__main__":
  main()
