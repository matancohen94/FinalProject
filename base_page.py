class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # finding an element and click on it
    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    # funtion for finding an element from list and click on it
    def click_element_from_list(self, locator_type, locator_value, index):
        self.driver.find_elements(locator_type, locator_value)[index].click()

    # finding an element and enter text into it
    def enter_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, locator_value).send_keys(text)

    # finding an element from list and enter text into it
    def enter_text_from_elements_list(self, locator_type, locator_value, text, index):
        self.driver.find_elements(locator_type, locator_value)[index].send_keys(text)
