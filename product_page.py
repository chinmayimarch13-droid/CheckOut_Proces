from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    add_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self):
        self.driver.find_element(*self.add_cart).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
