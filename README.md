# TraceWalker

## 概要
ラインレイヤに算出した『距離』、『移動時間』、『消費カロリー』をfeatureごとに属性付与するためのQGISプラグインです。  
  
下記式から消費カロリーの算出しています。  
`エネルギー消費量(kcal) = METs(強度) * 体重　* 時間(h) `   
※当プラグインは、普通歩行を対象としているのでMETsは3.0として設定しています。
  
消費カロリー算出参考資料：https://www.mhlw.go.jp/content/10904750/001171393.pdf

---

## プラグイン使用方法
1. 当プラグインを開いてください。  
![./icon.png](https://github.com/00ky00/TraceWalker/blob/main/icon.png)
2. 表示メニューにデータを入力してください。  
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

## アイコンについて
国土地理院地球地図日本を加工して作成：https://www.gsi.go.jp/kankyochiri/gm_jpn.html

---  
