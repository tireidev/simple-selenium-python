# ========================================================== #
# [処理名]
# 自動Google検索処理
# 
# [メソッド名]
# 1. def main_func(): メイン処理
# ========================================================== #

# ライブラリ定義
from modules.webdriver import chrome_webdriver
from modules.screenshot import screenshot
from modules.func import google_search

def main_func():

    # ChromeWebdriverの呼び出し
    class_chrome_webdriver = chrome_webdriver.ChromeWebdriver()
    obj_chrome_webdriver = class_chrome_webdriver.get_chrome_webdirver()

    # google自動検索処理
    class_google_serach = google_search.GoogleSearch(obj_chrome_webdriver)
    class_google_serach.main_func()

    # スクリーンショット生成処理
    class_screenshot = screenshot.Screenshot(obj_chrome_webdriver)
    class_screenshot.main_func()

# メイン処理
main_func()