# 自分のラズパイのローカルipをSlackで取得するためのプログラム

## 必要な物
- python3
- pip\(python3\)
- 外部に接続できるインターネット
----
ここから下は、特段の説明がない限り、Raspi（ラズパイ）での操作と想定してください。
## システムの導入
- ip\_announcerというディレクトリを自分が整理しやすい場所に置く
- `sudo pip install slackbot`\(pipはpython3のpipと仮定する\)で`slackbot`というモジュールをインストールする
- 次は/boot/mypiname.csvに名前を書き込む、やり方は複数ある。
  - \(自分のPCで\)microSDをカードリーダに差し込んで、パソコンに接続し、BOOTというディレクトリ\(あるいはフォルダ\)の中で mypiname.csv というファイルを作り、自分のラズパイの名前を一行一単語で書く
  - `sudo vim /boot/mypiname.csv`で自分のラズパイの名前を一行一単語で書く
  - アルファベットと日本語どちらでもいい

## 実行
- raspi\_ip\_announcerに入り、`python3 run.py`でフォアグラウンドで実行する
- あるいは`python3 run.py &`でバックグラウンドで実行する

## スタートアッププログラムにする
- raspi\_ip\_announcerのディレクトリを\[PATH\_TO\_IP\_ANNOUNCER\]と仮定する
- /etc/rc.local を編集して\(sudo権限が要る\)、最後の`exit 0`の前に、以下の文を追加してください

```
eval 'sudo -u pi python3 [PATH_TO_IP_ANNOUNCER]/run.py &'
```
上のコードは「sudoという権限でpiユーザでpython3を使ってrun.pyを実行する」という意味
- これでラズパイが起動するたびのにrun.pyが実行される

## /etc/rc.localが実行されない場合
Raspbian Jessieの場合、以上のようなやり方だけでは、`/etc/rc.local`というスクリプトがスタートアップで実行されない事がある。

解決策として「Slow Wait for network connection before completing boot」をオンにするだけでいい。

まずは`sudo raspi-config`で設定画面に入る。

`3 Boot Option -> B2 Wait for Network at Boot -> YES`

以上のように選択すると、設定がオンになる。

解決策の参考リンクは以下：<br>
[Jessie: rc.local vs. systemd](https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=122207)<br>
[RASPBIAN JESSIEで/etc/rc.localを動作させる方法](https://qiita.com/nuwaa/items/298ada62c4209ea7f9ca)

## 使い方(Slackでの操作)
- uec-programming.slack.comを開く
- 左のチャット一覧の中で「ダイレクトメッセージ」を探し、その隣のプラスボタンを押す
- ipbot を検索欄に入力して、ipbotというアプリを探す
- ipbot をクリックして、右の緑の「開始」ボタンを押す
- ipbotとのダイレクトメッセージの中で「help」と話すと、ヘルプ文が出てくる
- 「@ipbot pi\_name:自分のパイの名前」\(/boot/mypiname.csvに書き込んだ単語\)を送信すると、その名前のラズパイのローカルIPが帰ってくる

