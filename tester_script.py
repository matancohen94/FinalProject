from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from intro_registration_screen import IntroRegistrationScreen
from selenium.webdriver.chrome.options import Options
from home_screen import HomeScreen
from pick_business_screen import PickBusinessScreen
from sender_receiver_information_screen import SenderReceiverInformationScreen
import json


class Final_Project_Tester(TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        browser = data['browserType']
        if browser == "chrome":
            self.driver = webdriver.Chrome(service=Service('C:/Users/cohen/Downloads/chromedriver-win32/chromedriver'
                                                           '-win32/chromedriver.exe')
                                           , options=chrome_options)
        url = data['URL']
        self.driver.get(url)
        # implicitly wait
        self.driver.implicitly_wait(10)
        # page load timeout
        self.driver.set_page_load_timeout(15)
        self.intro_registration_screen = IntroRegistrationScreen(self.driver)
        self.home_screen = HomeScreen(self.driver)
        self.pick_business_screen = PickBusinessScreen(self.driver)
        self.sender_receiver_information_screen = SenderReceiverInformationScreen(self.driver)
        print('Final project tester is starting')

    def test1_intro_registration_screen(self):
        self.intro_registration_screen.click_registration_login_button()
        self.intro_registration_screen.click_registration_button()
        self.intro_registration_screen.enter_firstname_registration('מתן')
        self.intro_registration_screen.enter_email_registration('cohenmatan94@gmail.com')
        self.intro_registration_screen.enter_password_registration('QWaszx12')
        self.intro_registration_screen.enter_password_verification('QWaszx12')
        self.intro_registration_screen.click_policy_checkbox()
        self.intro_registration_screen.click_final_registration_button()
        # self.intro_registration_screen.first_name_assertion('מתן')

    def test2_home_screen(self):
        self.home_screen.click_sum_box()
        self.home_screen.click_sum_choice()
        self.home_screen.click_region_box()
        self.home_screen.click_region_choice()
        self.home_screen.click_category_box()
        self.home_screen.click_category_choice()
        self.home_screen.click_gift_finding_button()

    def test3_pick_business_screen(self):
        self.driver.get('https://buyme.co.il/search?budget=1&category=315&region=13')
        self.pick_business_screen.url_assertion()
        self.pick_business_screen.click_pick_business()
        self.pick_business_screen.enter_price(1000)
        self.pick_business_screen.click_choice_button()

    def test4_sender_receiver_information_screen(self):
        self.driver.get('https://buyme.co.il/money/349578?price=1000')
        self.sender_receiver_information_screen.click_for_someone_button()
        self.sender_receiver_information_screen.enter_receiver_name('יצחק')
        self.sender_receiver_information_screen.click_dropdown_events()
        self.sender_receiver_information_screen.click_event_choice()
        self.sender_receiver_information_screen.enter_blessing('יום הולדת שמח :)')
        # self.sender_receiver_information_screen.upload_picture_from_PC()
        self.sender_receiver_information_screen.click_continue_button()
        self.sender_receiver_information_screen.click_on_NOW_checkbox()
        self.sender_receiver_information_screen.click_on_sms_button()
        self.sender_receiver_information_screen.enter_receiver_phone_number('0523642152')
        self.sender_receiver_information_screen.enter_sender_name('מתן')
        self.sender_receiver_information_screen.enter_sender_phone_number('0526468906')
        # self.sender_receiver_information_screen.receiver_name_assertion('יצחק')
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()
        print('Final project tester is done successfully')
