# はじめに
ポートフォリオとしてQGISプラグインを作成しました。
当プラグインを一言で表すと『散歩ルートプランナー』です。


---  
# TraceWaler
ラインレイヤに対して以下属性テーブルを作成し、算出した値を付与するためのプラグインです。  
属性付与はfeatureごとにされます。  

---
# プラグイン使用方法

1. 当プラグインを開いてください。  
![./icon.png](https://github.com/00ky00/TraceWalker/blob/main/icon.png)
2. 表示メニューにデータを入力してください。  
![./docs/画面1](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E9%9D%A21.png)  
- Layer：ラインレイヤを選択してください。
- 歩行スピード(km/h)：移動時間を調べるのに必要になります。※歩行スピードが分からない場合、初期値4.8でも問題ありません。
- 体重(kg)：体重を入力してください。消費カロリーを調べるのに必要になります。

  
3. 設定後、OKを押して、以下画面が出たら完了です。  
![./docs/画面2](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E9%9D%A22.png)
  
実行後の属性テーブル  
![./docs/画面3](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E9%9D%A23.png)

カラムについて
- lenght：求めたfeatureの長さの値を格納
- time：求めた移動にかかる時間の値を格納
- kcal：求めた消費カロリーの値を格納
---  

# こだわり

1. 【ラインレイヤ以外を選択対象として表示しない設計】  
   ユーザーに使いやすいUiとエラーになりにくい設計
   ![./docs/画面5](https://github.com/00ky00/TraceWalker/blob/main/docs/%E7%94%BB%E9%9D%A25.png)

3. 【アイコン】


---  
# 改善点

---  

# アイコンについて
国土地理院地球地図日本を加工して作成：https://www.gsi.go.jp/kankyochiri/gm_jpn.html

---  
# 消費カロリーの算出方法

消費カロリーの算出方法として以下の式を使用。  
  
`エネルギー消費量(kcal) = METs(強度) * 体重　* 時間(h) * 1.05`  
  ※当プラグインは、普通歩行を対象としているのでMETsは3.0として設定しています。

---

# 付録

| TH1 | TH2 |
----|---- 
| TD1 | TD3 |
| TD2 | TD4 |









本プラグインで使われているicon.pngについては国土地理院地球地図日本を加工して作成(https://www.gsi.go.jp/kankyochiri/gm_jpn.html)
