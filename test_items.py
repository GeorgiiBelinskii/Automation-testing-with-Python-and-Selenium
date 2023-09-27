from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_has_button_add_to_busket(browser):
    browser.get(link)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed()
    time.sleep(20)