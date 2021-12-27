# atcoder-python

# 前提条件

Docker Dektopをインストールしていること

# 利用方法

1.下記コマンドで本リポジトリをローカルにクローンする

```shell
git clone git@github.com:hiyasichuka/atcoder-python.git
```

2.VSCodeでディレクトリを開く

```shell
cd atcoder-python
code .
```

3.左下の><マークを押下して、Repopen in Containerをクリックする

4.ターミナルをzshに切り替える

<img width="1034" alt="スクリーンショット 2021-12-27 16 46 27" src="https://user-images.githubusercontent.com/52185395/147448270-b60a6345-e8d1-4caa-a983-4a7d1c00ac8f.png">



# AtCoder参戦手順

---

１．AtCoderにログインする

```shell
acc login
# AtCoderへのログインパスワード認証を行う
```
<img width="544" alt="スクリーンショット 2021-12-27 16 00 28" src="https://user-images.githubusercontent.com/52185395/147444203-1743c864-8c51-4202-8306-bcf43e067a69.png">

---

2.online-judge-toolsにもログイン

```shell
oj login https://atcoder.jp/
# AtCoderのログインパスワード認証を行う
```
![image](https://user-images.githubusercontent.com/52185395/147448816-86bd9873-9eb8-4728-8cb0-02301e189396.png)

---

3．problemsフォルダに移動して、コンテンストディレクトリを生成する

```
cd problems
acc new abc100
# acc new {contestID}
# contestIDはコンテストURLの末尾にあるエンドポイント名
```

---

4．問題を解く

VSCodeのエクスプローラから、コンテストフォルダにあるpyファイルを開いてコーディングする。

---

5．テストする

```shell
oj t -c "python x.py"
```

<img width="890" alt="スクリーンショット 2021-12-27 17 01 29" src="https://user-images.githubusercontent.com/52185395/147449538-1bba3db1-ff87-4536-abc4-be7339918356.png">

---

6.AtCoderに解答を提出する

```shell
acc s
# 確認用文字列を打ち込んでEnterを押す
```

<img width="890" alt="スクリーンショット 2021-12-27 17 01 29" src="https://user-images.githubusercontent.com/52185395/147449763-6751ff6c-83ef-4d6e-becf-34083f678cc2.png">

---

7.ブラウザが立ち上がって採点される

![image](https://user-images.githubusercontent.com/52185395/147449840-81d2b572-5bc0-4f7b-aa5b-e485e0cb4724.png)

---
