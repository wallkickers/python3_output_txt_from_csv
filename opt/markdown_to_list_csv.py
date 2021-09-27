import csv

"""
 マークダウン→csvに変換
 input：markdown.csv
 output：list.csv
 command：python markdown_to_list_csv.py
 出力書式：
  | 1 | [タイトルA](リンクA) | [タイトルB](リンクB) |
  ↓
  タイトルA,リンクA,タイトルB,リンクB
"""
def main():
    """
    タイトルを取得
    @param string data
    @return string
    """
    def getTitle(data):
        return data.split('[')[1].split(']')[0]

    """
    リンクを取得
    @param string data
    @return string
    """
    def getLink(data):
        return data.split('(')[1].split(')')[0]

    OUTPUT_PATH = './data/'
    DATA_FILE = OUTPUT_PATH + 'markdown.csv'
    OUTPUT_FILE = OUTPUT_PATH + 'list.csv'
    output_list = []

    # csvファイル読み取り
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)

        # 空白削除
        reader = list(filter(None, reader))

        for index, line in enumerate(reader):
            # テーブル列が3列の場合
            if(line[0].count('|') > 3):
                # | 1 | [タイトルA](リンクA) | [タイトルB](リンクB) |
                if('ー' not in line[0]):
                    source = line[0].split('|')[2]
                    testCode = line[0].split('|')[3]

                    s1 = getTitle(source)
                    s2 = getLink(source)
                    s3 = getTitle(testCode)
                    s4 = getLink(testCode)
                    output_list.append([s1, s2, s3, s4])
                # | 1 | [タイトルA](リンクA) | ー |
                else:
                    source = line[0].split('|')[2]
                    s1 = getTitle(source)
                    s2 = getLink(source)
                    output_list.append([s1, s2, '', ''])
            # テーブル列が2列の場合
            #  | 1 | [タイトルA](リンクA) |
            else:
                s1 = getTitle(line[0])
                s2 = getLink(line[0])
                output_list.append([s1, s2])
    # csvファイルへ出力
    with open(OUTPUT_FILE, 'w', newline='') as f2:
        for line in output_list:
            writer = csv.writer(f2)
            writer.writerow(line)

if __name__ == "__main__":
  main()
