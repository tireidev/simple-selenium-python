import datetime

class Screenshot:

    def __init__(self, obj_chrome_webdriver):
        # Webdriverの指定
        self.obj_chrome_webdriver = obj_chrome_webdriver
        # ウィンドウサイズ(画像サイズ)の指定
        self.obj_chrome_webdriver.set_window_size(1920, 1080)
        self.path = "./img/"

    def main_func(self):
        
        # 現在時刻
        dt_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # スクショ作成
        self.obj_chrome_webdriver.save_screenshot(self.path+'capture_{}.png'.format(dt_now))