# TraceWalker

## 概要
ラインレイヤに算出した『距離』、『移動時間』、『消費カロリー』を地物ごとに属性付与するためのQGISプラグインです。  
  
下記式から消費カロリーの算出しています。   
`エネルギー消費量(kcal) = METs(強度) * 体重　* 時間(h) `   
※当プラグインは、普通歩行を対象としているのでMETsは3.0として設定しています。  
  
消費カロリー算出参考資料：https://www.mhlw.go.jp/content/10904750/001171393.pdf

---
## こだわり
直観的に分かりやすい設計
- メニュー画面：ラインレイヤ以外を表示しない。
- 付与される値：単位変換した値を付与する。
  - 1000m超えた場合、kmに単位変換。
  - 60秒を超え場合、分、60分超えたら時間に単位変換。

---
## 導入方法
1. QGISをダウンロード(https://qgis.org/ja/site/forusers/download.html)
2. このリポジトリをzipファイルでダウンロード。
3. QGISのプラグインの管理とインストールからダウンロードしたzipを読み込みます。
![./docs/画面4](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E9%9D%A24.png) 

---
## プラグイン使用方法
※データがない場合は、以下データをQGISにドラッグ＆ドロップして使用してください。  
./TraceWalker-main/TraceWalker-main/demo/test.geojson
1. 当プラグインを開いてください。  
![./icon.png](https://github.com/00ky00/TraceWalker/blob/main/icon.png)

3. 表示メニューにデータを入力してください。  
![./docs/画面1](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E5%83%8F1.png)  
- Layer：調べたいラインレイヤを選択してください。  
- 歩行スピード(km/h)：歩行スピードを入力してください。  
  ※歩行スピードが分からない場合、初期値4.8でも問題ありません。
- 体重(kg)：体重を入力してください。

3. 設定後、OKを押して、以下画面が出たら完了です。  
![./docs/画面2](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E9%9D%A22.png)  
  
実行後の属性テーブル  
![./docs/画面3](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E9%9D%A23.png)  

カラムについて
- lenght：featureの距離
- time：移動時間
- kcal：消費カロリー
  
---  
## デモ
![./demo/demo](https://github.com/00ky00/TraceWalker/blob/main/demo/demo.png)   

---  

## アイコンについて
国土地理院地球地図日本を加工して作成：https://www.gsi.go.jp/kankyochiri/gm_jpn.html

---  
