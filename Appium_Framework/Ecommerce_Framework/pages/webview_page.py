import time


class WebViewPage:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_webview(self):
        time.sleep(5)

        contexts = self.driver.contexts

        print(contexts)

        self.driver.switch_to.context(contexts[1])

    def open_amazon(self):
        self.driver.get("https://www.amazon.com")

    def switch_to_native(self):
        self.driver.back()

        self.driver.switch_to.context("NATIVE_APP")
