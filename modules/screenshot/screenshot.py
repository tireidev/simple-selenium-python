# ========================================================== #
# [処理名]
# スクリーンショット生成処理
# 
# [クラス名]
# Screenshot
# 
# [メソッド名]
# 1. def __init__(self, obj_chrome_webdriver): 初期化処理
# 2. main_func(self): メイン処理
# ========================================================== #

import datetime
from ..const import const

class Screenshot:

    def __init__(self, obj_chrome_webdriver):

        # Webdriverの指定
        self.obj_chrome_webdriver = obj_chrome_webdriver

        # ウィンドウサイズ(画像サイズ)の指定
        page_width = self.obj_chrome_webdriver.execute_script('return document.body.scrollWidth')
        page_height = self.obj_chrome_webdriver.execute_script('return document.body.scrollHeight')

        self.obj_chrome_webdriver.set_window_size(page_width, page_height)
        self.path = const.IMG_PATH

    def main_func(self):
        
        # 現在時刻
        dt_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        # スクショ作成
        self.obj_chrome_webdriver.save_screenshot(self.path+'capture_{}.png'.format(dt_now))