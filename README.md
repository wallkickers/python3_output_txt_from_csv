## python3_output_txt_from_csv
### 機能
##### A： csvファイルからデータを読み取り、txtファイルへマークダウン形式の表における行部分を出力するプログラム【output.py】
```
タイトル1,URL1     | 1 | [タイトル1](URL1) |
タイトル2,URL2  →  | 2 | [タイトル2](URL2) |
タイトル3,URL3     | 3 | [タイトル3](URL3) |
```

##### B： マークダウン形式で形式の表における行部分が記載されたcsvファイルからデータを読み取り、csvへ出力するプログラム【markdown_to_list_csv.py】
```
| 1 | [タイトル1](URL1) | [タイトル1'](リンク1') |     タイトル1,URL1,タイトル1',URL1'
| 1 | [タイトル2](URL2) | [タイトル2'](リンク2') |  →  タイトル2,URL2,タイトル2',URL2'
| 1 | [タイトル3](URL3) | [タイトル3'](リンク3') |     タイトル3,URL3,タイトル3',URL3'
```

##### C： csvファイルからデータを読み取り、txtファイルへマークダウン形式の表における行部分を出力するプログラム【output_add_column.py】
```
タイトル1,URL1,タイトル1',URL1'     | 1 | [タイトル1](URL1) | [タイトル1'](URL1') |
タイトル2,URL2,タイトル2',URL2'  →  | 2 | [タイトル2](URL2) | [タイトル2'](URL2') |
タイトル3,URL3,タイトル3',URL3'     | 3 | [タイトル3](URL3) | [タイトル3'](URL3') |
```

##### D： csvファイルの1行目をヘッダー,　以降の行を内容として出力するプログラム【output_table.py】
```
ヘッダー1,ヘッダー2,ヘッダー3       | ヘッダー1 | ヘッダー2 | ヘッダー3 |
内容1,内容2,内容3              →   | ------------- | ------------- | ------------- |
内容1,内容2,内容3                  | 内容1 | 内容2 | 内容3 |
                                  | 内容1 | 内容2 | 内容3 |
```

#### 実行環境
| 環境 | ver. |
| ------------- | ------------- |
| Windows10 Pro | 20H2 |
| Docker desktop | 3.6.0 |

#### フォルダ構成
python  
&nbsp;&nbsp;├ Dockerfile  
&nbsp;&nbsp;├ docker-compose.yml  
&nbsp;&nbsp;└ opt  
&nbsp;&nbsp;&nbsp;&nbsp;├ output.py  
&nbsp;&nbsp;&nbsp;&nbsp;├ output_table.py  
&nbsp;&nbsp;&nbsp;&nbsp;├ output_add_column.py  
&nbsp;&nbsp;&nbsp;&nbsp;├ markdown_to_list_csv.py  
&nbsp;&nbsp;&nbsp;&nbsp;├ list.csv  
&nbsp;&nbsp;&nbsp;&nbsp;├ markdown_to_list.csv  
&nbsp;&nbsp;&nbsp;&nbsp;└ data  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├ list.csv  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├ markdown.csv  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ output.txt  

#### 環境構築
1. docker-compose.ymlのあるディレクトリで`docker-compose up -d` を実行

### How to (使い方)
#### A： csvファイルからデータを読み取り、txtファイルへマークダウン形式の表における行部分を出力するプログラム(output.py)
##### 1. csvファイルの用意
1. 1列目にリンクのテキスト、2列目にリンクのURLを記入

##### 2. txtファイルの出力
1. `docker ps` でコンテナIDを確認
1. `docker exec -it {コンテナID} bash` でコンテナに入る
1. `cd opt` でoptディレクトリへ移動
1. opt/data/ディレクトリ内にoutput.txtが出力されていることを確認

#### B： マークダウン形式で形式の表における行部分が記載されたcsvファイルからデータを読み取り、csvへ出力するプログラム(markdown_to_list_csv.py)
##### 1. csvファイルの用意
1. markdown.csvの1列目にマークダウン形式で記述された表における行を記入

##### 2. csvファイルの出力
1. `python markdown_to_list_csv.py` で実行。list.csvを出力  
　（コンテナへの入り方は機能Aの手順2と同じ）

#### C： csvファイルからデータを読み取り、3列目が入力されている場合は3カラム目もtxtファイルへマークダウン形式の表における行部分を出力するプログラム(output_add_column.py)

##### 1. csvファイルの用意
1. 1列目にリンクのテキスト、2列目にリンクのURLを記入
1. 3列目にリンクのテキスト、4列目にリンクのURLを記入

##### 2. txtファイルの出力
1. `python output_add_column.py` で実行。opt/data/ディレクトリ内にoutput.txtが出力されていることを確認  
　（コンテナへの入り方は機能Aの手順2と同じ）
 
#### D： csvファイルの1行目をヘッダー,　以降の行を表の内容として出力するプログラム(output_table.py)

##### 1. csvファイルの用意
1. 1列目に表のヘッダー部、2列目以降に表の内容部を記入

##### 2. txtファイルの出力
1. `python output_table.py` で実行。opt/data/ディレクトリ内にoutput.txtが出力されていることを確認  
　（コンテナへの入り方は機能Aの手順2と同じ）

#### 補足
- 列数を増やしたい場合は出力フォーマットを記述している箇所の `|` を増やすことで追加が可能です。（outpyt.py 18行目付近）  
また、記述内容を変更したいときもこの辺りを変更すれば良いと思います。

```
s = f'| {str(index+1)} | [{line[0]}]({line[1]}) |\n'
↓
s = f'| {str(index+1)} | [{line[0]}]({line[1]}) | memo |\n'
```

#### 参考
- [DockerでPython実行環境を作ってみる](https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5)
- [Pythonの文字列における変数展開を現役エンジニアが解説【初心者向け】](https://techacademy.jp/magazine/22721)
- [テキストファイルへ書き込む](https://www.javadrive.jp/python/file/index3.html)
