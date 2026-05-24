from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from utilities.base_page import BasePage


class HomePage(BasePage):
    name = (By.ID, "com.androidsample.generalstore:id/nameField")

    female = (By.XPATH, "//android.widget.RadioButton[@text='Female']")

    country_dropdown = (By.ID, "android:id/text1")

    argentina = (
        By.XPATH, "//android.widget.TextView[@text='Argentina']")

    lets_shop = (By.ID, "com.androidsample.generalstore:id/btnLetsShop")

    def enter_name(self, text):
        self.wait_for_element(self.name).send_keys(text)

    def select_gender(self):
        self.wait_for_clickable(self.female).click()

    def select_country(self):
        self.wait_for_clickable(self.country_dropdown).click()

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector()).scrollIntoView(text("Argentina"));')

        self.wait_for_clickable(self.argentina).click()

    def click_lets_shop(self):
        self.wait_for_clickable(self.lets_shop).click()
