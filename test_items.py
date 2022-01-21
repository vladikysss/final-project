import time

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/agile-retrospective_168/"

def test_Add_to_cart_button(browser):
    browser.get(link)
    text_button = browser.find_elements_by_xpath("//button [@class = 'btn btn-lg btn-primary btn-add-to-basket']")
    assert len(text_button) == 1, 'Нет элемента'

