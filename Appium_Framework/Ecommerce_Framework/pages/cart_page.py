from selenium.webdriver.common.by import By
from utilities.base_page import BasePage


class CartPage(BasePage):
    product_price = (
        By.ID, "com.androidsample.generalstore:id/productPrice")

    total_amount = (
        By.ID, "com.androidsample.generalstore:id/totalAmountLbl")

    terms_button = (
        By.ID, "com.androidsample.generalstore:id/termsButton")

    accept_button = (By.ID, "android:id/button1")

    checkbox = (By.CLASS_NAME, "android.widget.CheckBox")

    proceed_button = (
        By.ID,"com.androidsample.generalstore:id/btnProceed")

    def verify_total(self):
        prices = self.driver.find_elements(*self.product_price)

        total = 0

        for price in prices:
            amount = float(price.text[1:])
            total += amount

        displayed_total = float(
            self.driver.find_element(*self.total_amount).text[1:])

        assert total == displayed_total

    def accept_terms(self):
        ele = self.driver.find_element(*self.terms_button)

        self.driver.execute_script(
            "mobile: longClickGesture",
            {"elementId": ele.id,"duration": 2000})

        self.wait_for_clickable(self.accept_button).click()

    def proceed_checkout(self):
        self.wait_for_clickable(self.checkbox).click()

        self.wait_for_clickable(self.proceed_button).click()
