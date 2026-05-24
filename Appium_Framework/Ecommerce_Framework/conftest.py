import os
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options


# =========================================
# DRIVER FIXTURE
# =========================================

@pytest.fixture(scope="function")
def driver():

    options = UiAutomator2Options()
    options.chromedriver_executable = r"C:\Users\HP\Documents\Appium Chrome Driver\chromedriver.exe"
    options.platform_name = "Android"
    options.device_name = "Pixel 8a"
    options.automation_name = "UiAutomator2"

    options.app = (
        r"E:\Appium_Eclipse\Appium\src\test\java\resources\General-Store.apk"
    )

    options.auto_grant_permissions = True

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call":

        if report.failed:

            driver = item.funcargs.get("driver")

            if driver:

                screenshot = driver.get_screenshot_as_base64()

                html = f'''
                <div>
                    <img src="data:image/png;base64,{screenshot}"
                    width="300"
                    height="600"
                    onclick="window.open(this.src)"
                    align="right"/>
                </div>
                '''

                extra.append(pytest_html.extras.html(html))

        report.extra = extra