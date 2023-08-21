from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from base_page import BasePage


class IntroRegistrationScreen(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # adding driver
    driver = webdriver.Chrome(service=Service('C:/Users/cohen/Downloads/chromedriver-win32/chromedriver'
                                              '-win32/chromedriver.exe'))

    # click on "כניסה/הרשמה" button
    def click_registration_login_button(self):
        self.click_element(By.CLASS_NAME, 'notSigned')

    # click on "להרשמה" button
    def click_registration_button(self):
        self.click_element(By.CSS_SELECTOR, 'span[aria-label=להרשמה]')

    # enter on "שם פרטי" box
    def enter_firstname_registration(self, first_name):
        self.enter_text(By.ID, 'ember1917', first_name)

    # enter on "מייל" box
    def enter_email_registration(self, email):
        self.enter_text(By.ID, 'ember1924', email)

    # enter on "סיסמא" box
    def enter_password_registration(self, password):
        self.enter_text(By.ID, 'valPass', password)

    # enter on "אימות סיסמא" box
    def enter_password_verification(self, password):
        self.enter_text(By.ID, 'ember1938', password)

    # agreement on website policy and terms of use
    def click_policy_checkbox(self):
        self.click_element(By.ID, 'ember1944')

    # click on "BUYME-הרשמה ל" button
    def click_final_registration_button(self):
        self.click_element(By.ID, "ember1948")

    # assert first name
    # def first_name_assertion(self, first_name):
    #     expected_first_name = first_name
    #     assert  self.driver.find_element(locate_with(By.ID, 'ember1917')).text == expected_first_name

    driver.quit()
