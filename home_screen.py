from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from base_page import BasePage
import time


class HomeScreen(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # adding driver
    driver = webdriver.Chrome(service=Service('C:/Users/cohen/Downloads/chromedriver-win32/chromedriver'
                                              '-win32/chromedriver.exe'))

    # dropdown sum opening
    def click_sum_box(self):
        time.sleep(1)
        self.click_element_from_list(By.CLASS_NAME, 'selected-name', 0)

    # sum choice
    def click_sum_choice(self):
        time.sleep(1)
        self.click_element(By.ID, 'ember1075')

    # dropdown region opening
    def click_region_box(self):
        time.sleep(1)
        self.click_element_from_list(By.CLASS_NAME, 'selected-name', 1)

    # region choice
    def click_region_choice(self):
        time.sleep(1)
        self.driver.find_element(By.ID, 'ember1111')

    # dropdown category opening
    def click_category_box(self):
        time.sleep(1)
        self.click_element_from_list(By.CLASS_NAME, 'selected-name', 2)

    # category choice
    def click_category_choice(self):
        time.sleep(1)
        self.click_element(By.ID, 'ember1180')

    # click on "תמצאו לי מתנה" button
    def click_gift_finding_button(self):
        time.sleep(1)
        self.click_element(By.CSS_SELECTOR, 'a[rel=nofollow]')

    driver.quit()
