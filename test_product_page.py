from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_name, product_price = page.get_product_info()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_cart(product_name, product_price)
