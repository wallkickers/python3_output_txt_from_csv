### python3_output_txt_from_csv
csvファイルからデータを読み取り、txtファイルへマークダウン形式の表における行部分を出力するプログラム

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
