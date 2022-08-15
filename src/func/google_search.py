from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearch:

    def __init__(self, obj_chrome_webdriver):
        self.obj_chrome_webdriver = obj_chrome_webdriver

    def main_func(self):
        # Google URL
        self.obj_chrome_webdriver.get('https://www.google.com/')
        
        # 検索ボックスを特定
        element_google_searchbox = self.obj_chrome_webdriver.find_element(By.NAME, 'q')

        # 「Selenium」と入力して、「Enter」を押す
        element_google_searchbox.send_keys('Selenium' + Keys.RETURN)