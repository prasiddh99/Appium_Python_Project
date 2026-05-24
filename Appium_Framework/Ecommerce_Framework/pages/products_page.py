from selenium.webdriver.common.by import By
from utilities.base_page import BasePage


class ProductsPage(BasePage):
    add_to_cart = (
        By.XPATH,
        "//android.widget.TextView[@text='ADD TO CART']")

    cart_button = (
        By.ID, "com.androidsample.generalstore:id/appbar_btn_cart")

    def add_products_to_cart(self):
        products = self.driver.find_elements(*self.add_to_cart)

        products[0].click()

        products = self.driver.find_elements(*self.add_to_cart)

        products[0].click()

    def open_cart(self):
        self.wait_for_clickable(self.cart_button).click()
