# Selenium(Python)の使い方まとめ
Selenium(Python)の簡易的な使い方をまとめていきます。

## 想定利用者
- Seleniumを活用してみたい方

## 前提
- ローカル端末にWindowsを利用する
- 使用ブラウザはGoogle Chromeを利用する
- Seleniumのインストールコマンドはpowershell上で実行する
- ユースケースとしては、Googleで「Selenium」と検索し、表示結果をキャプチャするケースを想定

## 事前準備
1. ローカル端末にPythonをインストールする
   1. Pythonのインストーラをは[こちら](https://www.python.org/)

2. Google Chromeのバージョンを確認し、Chrome Driverをインストールする
   1. Google Chromeのバージョン確認は[こちら](chrome://settings/help)
   2. Chrome Driverのインストーラは[こちら](https://chromedriver.chromium.org/downloads) 
      1. インストーラはchromedriver_win32.zipを利用
      2. 解凍した実行ファイルは適当な場所に配置すること 例) C:\tools\chromedriver.exe

3. 以下のコマンドでseleniumをインストールする
```
python -m pip install --upgrade pip
pip install selenium
```
Windowsでwslを利用してる場合は以下のコマンドを利用
```
python -m pip install --upgrade pip
pip3 install selenium
```

以下のコマンドでseleniumが表示されることを確認する。
```
pip list
```