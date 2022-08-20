# ========================================================== #
# [処理名]
# ChromeWebdriver生成処理
# 
# [クラス名]
# ChromeWebdriver
# 
# [メソッド名]
# 1. def __init__(self): 初期化処理
# 2. def get_chrome_webdirver(self): chrome webdriver返却処理
# ========================================================== #

# ライブラリ定義
from selenium import webdriver
from selenium.webdriver.chrome import service
from ..const import const

class ChromeWebdriver:

    def __init__(self):

        # webdriverのパスを指定
        chrome_service = service.Service(executable_path=const.CHROME_DRIVER)

        # Chromeオプション設定用クラスの生成
        chrome_options = webdriver.ChromeOptions()

        # 以下のエラーを防止するため
        #  [3000:7696:0816/212549.767:ERROR:device_event_log_impl.cc(214)] [21:25:49.767] Bluetooth: bluetooth_adapter_winrt.cc:1074 Getting Default Adapter failed.
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # スクロールバー非表示処理
        chrome_options.add_argument('--hide-scrollbars')

        # ブラウザ非表示処理
        chrome_options.add_argument('--headless')

        # Chromeオプション設定
        self.chrome_webdriver = webdriver.Chrome(service=chrome_service, options=chrome_options)


    def get_chrome_webdirver(self):

        # chrome webdriverを返却
        return self.chrome_webdriver