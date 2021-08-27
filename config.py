from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent



def iniciachrome():
    ua = UserAgent()
    userAgent = ua.random

    chrome_options = Options()
    chrome_options.headless = False
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("user-data-dir=C:/Users/gabri/AppData/Local/Google/Chrome/User Data/Default")
    DRIVER_PATH = 'chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)

    return driver

