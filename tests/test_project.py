from pages.main_page import *
from data import *


def test_company_logo(driver, wait):
    '''TC-01 The Company Logo is active and works correctly'''
    web_page = MainPage(driver, wait)
    link_page = PricingPage(driver, wait)
    web_page.open()
    link_page.open()
    link_page.company_logo()
    assert driver.current_url == main_page


def test_active_link(driver, wait):
    '''TC-02 Verify if the header part is always visible and active link is highlighted'''
    web_page = MainPage(driver, wait)
    link_page = ExtrasPage(driver, wait)
    web_page.open()
    link_color = link_page.link_color()
    link_page.open()
    active_link_color = link_page.link_color()
    assert link_color != active_link_color


def test_login_to_account(driver, wait):
    '''TC-04 Verify if the registered user can log on the System'''
    web_page = MainPage(driver, wait)
    link_page = LoginPage(driver, wait)
    web_page.open()
    link_page.open()
    link_page.enter_email(email)
    link_page.enter_password(password)
    link_page.click_eye()
    link_page.submit_login()
    link_page.login_confirm()


def test_icon_platform(driver, wait):
    '''TC-07 Validate if the icons for different Platform are active and navigates correctly'''
    web_page = MainPage(driver, wait)
    link_page = DownloadPage(driver, wait)
    web_page.open()
    link_page.icon()
    link_page.next_tab()
    link_page.text()
    link_page.previous_tab()


def test_subscribe(driver, wait):
    '''TC-13 Validate if the user can subscribe for newsletter'''
    web_page = MainPage(driver, wait)
    link_page = SubscribePage(driver, wait)
    web_page.open()
    link_page.enter_email(email_test)
    link_page.submit_subscribe()
    link_page.subcribe_confirm()


#  java -jar C:\Users\j\Downloads\jenkins.war
