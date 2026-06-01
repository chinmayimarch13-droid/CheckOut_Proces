from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from testdata.test_data import *

def test_checkout(setup):

    driver = setup
    driver.get(url)

    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    product = ProductPage(driver)
    product.add_to_cart()
    product.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_first_name(firstname)
    checkout.enter_last_name(lastname)
    checkout.enter_postal_code(zipcode)
    checkout.click_continue()
    checkout.click_finish()

    assert "checkout-complete" in driver.current_url
