
# ライブラリ定義
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from ..const import const

class ChromeWebdriver:

    def __init__(self):

        chrome_service = fs.Service(executable_path=const.CHROME_DRIVER)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.chrome_webdriver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def get_chrome_webdirver(self):
        return self.chrome_webdriver