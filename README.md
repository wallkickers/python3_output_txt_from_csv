### python3_output_txt_from_csv
csvファイルからデータを読み取り、txtファイルへマークダウン形式の表における行部分を出力するプログラム

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
&nbsp;&nbsp;&nbsp;&nbsp;└ output.py  
&nbsp;&nbsp;&nbsp;&nbsp;└ list.csv  

#### 環境構築
1. docker-compose.ymlのあるディレクトリで`docker-compose up -d` を実行

#### csvファイルからデータを読み取り、txtファイルへ出力
##### 1. csvファイルの用意
1. 1列目にリンクのテキスト、2列目にリンクのURLを記入

##### 2. txtファイルの出力
1. `docker ps` でコンテナIDを確認
1. `docker exec -it {コンテナID} bash` でコンテナに入る
1. `cd opt` でoptディレクトリへ移動
1. optディレクトリ内にoutput.txtが出力されていることを確認

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
