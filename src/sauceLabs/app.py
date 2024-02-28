import time
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sauceLabs.browserController import BrowserController
from sauceLabs.constant import BrowserType
from sauceLabs.config import APPLICATION_URL



def start():
    browser = BrowserController(BrowserType.EDGE)

    try:

        browser.open_url(url=APPLICATION_URL)
        browser.make_browser_max_window_size()
        login(browser)
        check_product_page_availability(browser)

    except Exception as ex:
        print(f"Exception during execution: {ex}")
    
    finally:

        browser.hold_execution(seconds=5)
        browser.close()
        browser.kill()

 
def login(browser : BrowserController):
    browser.wait_for_element_presence_or_visibility(By.ID, "user-name")
    browser.send_keys(By.ID,"user-name","standard_user")
    browser.send_keys(By.ID,"password","secret_sauce")
    browser.click(By.ID, "login-button")

def check_product_page_availability(browser : BrowserController):
    app_title = browser.get_text(By.CLASS_NAME, "app_logo")

    if(app_title != "Swag Labs"):
        raise(ValueError("Wrong value errors validation"))

#dummy comment
