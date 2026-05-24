from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.webview_page import WebViewPage


class TestEcommerceHybrid:

    def test_complete_flow(self, driver):
        home = HomePage(driver)

        home.enter_name("Parth")

        driver.hide_keyboard()

        home.select_gender()

        home.select_country()

        home.click_lets_shop()

        print("Home page completed")

        products = ProductsPage(driver)

        products.add_products_to_cart()

        print("Products added")

        products.open_cart()

        cart = CartPage(driver)

        cart.verify_total()

        print("Total verified")

        cart.accept_terms()

        cart.proceed_checkout()

        print("Checkout completed")

        webview = WebViewPage(driver)

        webview.switch_to_webview()

        webview.open_amazon()

        webview.switch_to_native()

        print("Hybrid app test completed")
