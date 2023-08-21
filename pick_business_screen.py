from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from base_page import BasePage


class PickBusinessScreen(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # adding driver
    driver = webdriver.Chrome(service=Service('C:/Users/cohen/Downloads/chromedriver-win32/chromedriver'
                                              '-win32/chromedriver.exe'))

    # assert url
    def url_assertion(self):

        expected_url = 'https://buyme.co.il/search?budget=1&category=315&region=13'
        assert expected_url == self.driver.current_url

    # pick business
    def click_pick_business(self):
        self.click_element_from_list(By.CLASS_NAME, 'bottom', 4)

    # price choice
    def enter_price(self, price):
        self.enter_text(By.CSS_SELECTOR, 'input[type=tel]', price)

    # click on "בחירה" button
    def click_choice_button(self):
        self.click_element(By.CSS_SELECTOR, 'button[type=submit]')

    driver.quit()
