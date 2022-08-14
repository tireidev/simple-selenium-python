# ========================================================== #
# [処理名]
# 自動Google検索処理
# ========================================================== #

# ライブラリ定義
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs

CHROME_DRIVER = 'C:/tools/chromedriver.exe'
chrome_service = fs.Service(executable_path=CHROME_DRIVER)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_webdriver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Google URL
chrome_webdriver.get('https://www.google.com/')
 
# 検索ボックスを特定
element_google_searchbox = chrome_webdriver.find_element(By.NAME, 'q')

# 「Selenium」と入力して、「Enter」を押す
element_google_searchbox.send_keys('Selenium' + Keys.RETURN)
