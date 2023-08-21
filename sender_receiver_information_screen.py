from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from base_page import BasePage
from allure_commons.types import AttachmentType
import allure


class SenderReceiverInformationScreen(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # adding driver
    driver = webdriver.Chrome(service=Service('C:/Users/cohen/Downloads/chromedriver-win32/chromedriver'
                                              '-win32/chromedriver.exe'))

    # click on "למישהו אחר" button
    def click_for_someone_button(self):
        self.click_element(By.ID, 'ember1370')

    # receiver name
    def enter_receiver_name(self, receiver_name):
        self.enter_text(By.ID, 'friendName', receiver_name)

    # dropdown events
    def click_dropdown_events(self):
        self.click_element(By.CLASS_NAME, 'selected-name')

    # event choice
    def click_event_choice(self):
        self.click_element(By.ID, 'ember1802')

    # enter a blessing
    def enter_blessing(self, words):
        self.enter_text(By.ID, 'ember1385', words)
        allure.attach(self.driver.get_screenshot_as_png(), name=" blessing text", attachment_type=AttachmentType.PNG)

    # def upload_picture_from_PC(self):
    #     pic_path = 'C:/Users/cohen/OneDrive/שולחן העבודה/download.jpg'
    #     self.click_element(By.XPATH, '//input[@type="file"]').send_keys(pic_path)

    # click on "המשך" button
    def click_continue_button(self):
        self.click_element(By.ID, 'ember1395')

    # click on "עכשיו" checkbox
    def click_on_NOW_checkbox(self):
        self.click_element(By.CLASS_NAME, 'check')

    # click on SMS button
    def click_on_sms_button(self):
        self.click_element(By.CSS_SELECTOR, 'svg[gtm=method-sms]')

    # gift receiver's phone number box
    def enter_receiver_phone_number(self, receiver_phone):
        self.enter_text(By.ID, 'sms', receiver_phone)

    # gift sender's name box
    def enter_sender_name(self, sender_name):
        self.enter_text(By.CSS_SELECTOR, 'input[type=text', sender_name)

    # gift sender's phone number box
    def enter_sender_phone_number(self, sender_phone):
        self.enter_text_from_elements_list(By.CSS_SELECTOR, 'input[data-parsley-mobile=mobile]'
                                           , sender_phone, 2)

    # assert receiver name
    # def receiver_name_assertion(self, receiver_name):
    #     expected_receiver_name = receiver_name
    #     assert expected_receiver_name == receiver_name

    driver.quit()
