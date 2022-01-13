# Interrupt_Negative_pkg
千葉工業大学
未来ロボティクス学科2年後期
 
ロボットシステム学課題２
 
講義動画：ロボットシステム学第10回(<https://www.youtube.com/watch?v=PL85Pw_zQH0>)を見ながら、その手順に則って作成。
## コードについて
千葉工業大学　未来ロボティクス学科准教授　上田隆一先生(<https://github.com/ryuichiueda>)のコードの一部を改変したものです。

## オリジナルの変更点
* /dev/myled0　をcatしたときの出力文字を変更。
 
* LED点灯のパターンを追加。

## デモ映像
<https://youtu.be/TQ50Kr4OWGU>

## 動作確認環境
OS ...Ubuntu 20.04 LTS
 
ハード...Raspberry Pi4

## 使用方法
* ハードのセッティング
 
　LEDのアノードをRaspberry Pi4
のGPIO25ピンに繋ぎ、カソードをGNDに接続する。LEDには200Ω程度の抵抗を挟むことが理想である。
 
 この図では赤いコードがアノード、青いコードがカソードになっている。
![IMG_E0642](https://user-images.githubusercontent.com/92071428/147917005-24eb0873-2156-4357-9fed-8f7461dc2b2f.JPG)
* コンパイル
 
```$ make```
* インストール

```$ sudo insmod myled.ko```
* 権限の設定
 
 ```$ sudo chmod 666 /dev/myled0``` 
* LEDの点灯
 
 ```$ echo (0~9,-) > /dev/myled0```
* アンインストール

```$ sudo rmmod myled```
 
```$ make clean```

## ライセンス
 BSD-3-Clause License

## 参考
READMEの書き方(<https://laraweb.net/surrounding/7477/>)
 
 【GitHub】README.md に画像を表示させる簡単な方法(<https://qiita.com/r_midori/items/2c4feb5de05535441bc8>)
