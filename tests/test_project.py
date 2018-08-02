from pages.main_page import MainPage
from tests.data import *



def test_company_logo(driver, wait):
    '''TC-01 The Company Logo is active and works correctly'''
    web_page = MainPage(driver, wait)
    web_page.open()
    web_page.find_company_logo()
    web_page.open_link_Pricing()
    web_page.find_company_logo()
    assert driver.current_url == main_page


def test_active_link(driver, wait):
    '''TC-02 Verify if the header part is always visible and active link is highlighted'''
    web_page = MainPage(driver, wait)
    web_page.open()
    link_color = web_page.link_color()
    web_page.open_link_Pricing()
    active_link_color = web_page.link_color()
    assert link_color != active_link_color


def test_login_to_account(driver, wait):
   '''TC-04 Verify if the registered user can log on the System'''
   web_page = MainPage(driver, wait)
   web_page.open()
   web_page.open_login_form()
   web_page.enter_email(email)
   web_page.enter_password(password)
   web_page.click_eye()
   web_page.submit_login()
   web_page.login_confirm()


def test_icon_platform(driver, wait):
    '''TC-07 Validate if the icons for different Platform are active and navigates correctly'''
    web_page = MainPage(driver, wait)
    web_page.open()
    web_page.click_icon()
    web_page.next_tab()
    web_page.find_text()
    web_page.previous_tab()


def test_subscribe(driver, wait):
    '''TC-13 Validate if the user can subscribe for newsletter'''
    web_page = MainPage(driver, wait)
    web_page.open()
    web_page.enter_email_for_subscribe(email_test)
    web_page.submit_subscribe()
    web_page.subcribe_confirm()

