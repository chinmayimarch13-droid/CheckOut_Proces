from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")

    def enter_first_name(self, fname):
        self.driver.find_element(*self.first_name).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element(*self.last_name).send_keys(lname)

    def enter_postal_code(self, code):
        self.driver.find_element(*self.postal_code).send_keys(code)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()
