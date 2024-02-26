import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from sauceLabs.constant import BrowserType



class BrowserController:

    def __init__(self,browser_type : BrowserType):

        self.driver : WebDriver = None

        if browser_type == BrowserType.FIREFOX:
            self.driver=webdriver.Firefox()           
        elif browser_type == BrowserType.CHROME:
            self.driver=webdriver.Chrome()
        elif browser_type == BrowserType.EDGE:
            self.driver=webdriver.Edge()
        elif browser_type == BrowserType.SAFARI:
            self.driver=webdriver.Safari()
            
        else:
            raise NameError('Only firefox,Chrome,Edge and Safari are supported')

    def find_element(self,element_type : By, value) -> WebElement:
        element : WebElement = None
        element = self.driver.find_element(element_type, value=value)
        return element

    def find_elements(self, element_type : By ,value) -> list[WebElement]:
        elements : list[WebElement] = []
        elements = self.driver.find_elements(element_type, value=value)
        return elements

    def wait_for_element_presence_or_visibility(self,element_type : By, element_details, check_presence = False, wait_timeout=6):

        if(check_presence):
            # Useful for: Ensuring an element exists, even if it's hidden, off-screen, or not yet ready for interaction.
            WebDriverWait(self.driver,wait_timeout,1).until(EC.presence_of_element_located((element_type, element_details)))
        else:
            # Waiting for elements that should be visible and ready for interaction, like buttons, links, or text fields.
            WebDriverWait(self.driver,wait_timeout,1).until(EC.visibility_of_element_located((element_type, element_details)))

    def wait_for_text_presence(self,element_type : By, element_details, text, check_element_value = True, wait_timeout=6):        
        
        if(check_element_value):
            # Use cases: Waiting for input fields, text areas, dropdown menus to receive user input or dynamically update their values.
            WebDriverWait(self.driver,wait_timeout,1).until(EC.text_to_be_present_in_element_value((element_type, element_details),text))
        else:
            # Use cases: Waiting for headings, labels, paragraphs, or any element where the text content is relevant.
            WebDriverWait(self.driver,wait_timeout,1).until(EC.text_to_be_present_in_element((element_type, element_details),text))


    def open_url(self,url):
        self.driver.get(url)

    def make_browser_max_window_size(self):
        self.driver.maximize_window()

    def set_browser_window_size(self,width,height):
        self.driver.set_window_size(width,height)

    def send_keys(self,element_type : By, element_details,text):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        e1.clear()
        e1.send_keys(text)

    def clear(self,element_type : By,element_details):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        e1.clear()

    def click(self,element_type : By,element_details):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        e1.click()

    def right_click(self,element_type : By,element_details):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        ActionChains(self.driver).context_click(e1).perform()

    def move_element(self,element_type : By,element_details):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        ActionChains(self.driver).move_to_element(e1).perform()

    def double_click(self,element_details,element_type):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        ActionChains(self.driver).double_click(e1).perform()

    def  drag_and_drop(self,element_type_e1,e1,element_type_e2,e2):
        self.wait_for_element_presence_or_visibility(element_type_e1,e1)
        eme1=self.find_element(element_type_e1,e1)
        self.wait_for_element_presence_or_visibility(element_type_e2,e2)
        eme2=self.find_element(element_type_e2,e2)
        ActionChains(self.driver).drag_and_drop(eme1,eme2).perform()

    def click_text(self,text):
        e1 = self.find_element(By.LINK_TEXT, text)
        e1.click()

    def close(self):
        self.driver.close()

    def kill(self):
        self.driver.quit()

    def f5(self):
        self.driver.refresh()

    def js(self,sprit):
        self.driver.execute_script(sprit)

    def get_attribute(self, element_type,element_details, attribute):
        e1=self.find_element(element_type,element_details)
        return e1.get_attribute(attribute)

    def get_text(self,element_type : By,element_details):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        return e1.text

    def is_element_displayed_to_user(self,element_type : By,element_details):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        e1=self.find_element(element_type,element_details)
        return e1.is_displayed()

    def get_title(self):
        return self.driver.title

    def get_screen(self,file_path):
        self.driver.get_screenshot_as_file(file_path)

    def wait(self,element_type : By,element_details):
        self.driver.implicitly_wait((element_type,element_details))

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, element_type,element_details):
        self.wait_for_element_presence_or_visibility(element_type,element_details)
        if1=self.find_element(element_type,element_details)
        self.driver.switch_to.frame(if1)

    def hold_execution(self, seconds = 5):
        time.sleep(seconds)