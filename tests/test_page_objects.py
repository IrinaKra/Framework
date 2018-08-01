from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from allure.constants import AttachmentType

class MainPage:

   def __init__(self, driver):
       self.driver = driver

   def open(self):
       self.driver.get('https://www.vpnunlimitedapp.com/en')
       self.driver.set_window_size(1920, 1080) # if the browser window is not fullscreen, the header menu is not available
       return self

   def find_company_logo(self):
       self.driver.find_element_by_xpath("//img[@class='sm-hide']").click()

   def open_link_Pricing(self):
       self.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']/descendant::a[contains(text(),'Pricing')]").click()

   def open_login_form(self, wait):
       self.driver.find_element_by_xpath("//a[text()='Sign In']").click()
       wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-popup--container']")))
       return self

   def enter_email(self, email):
       self.driver.find_element_by_xpath("//input[@name='login']").send_keys(email)
       return self

   def enter_password(self, password):
       self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
       return self

   def click_eye(self):
       self.driver.find_element_by_xpath("//span[@class='icon-font-eye']").click()

   def submit_login(self):
       self.driver.find_element_by_xpath("//button[@type='submit']").click()

   def click_icon(self):
       self.driver.find_element_by_xpath("//img[@alt='VPN Unlimited for macOS']").click()

   def find_text(self, wait):
       wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()=' for macOS']")))
       return self

   def enter_email_for_subscribe(self, email_test):
       self.driver.find_element_by_xpath("//input[@name='email']").send_keys(email_test)
       return self

   def submit_subscribe(self):
       self.driver.find_element_by_xpath("//label[@class='footer_input_btn_label']").click()
       return self


main_page = 'https://www.vpnunlimitedapp.com/en'

def test_company_logo(driver):
    '''TC-01 The Company Logo is active and works correctly'''
    web_page = MainPage(driver)
    web_page.open()
    with allure.step('Main page'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    web_page.find_company_logo()
    web_page.open_link_Pricing()
    with allure.step('Pricing page'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    web_page.find_company_logo()
    with allure.step('Return to main page'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    assert driver.current_url == main_page


el = "//a[text()='Extras']"

def test_active_link(driver):
    '''TC-02 Verify if the header part is always visible and active link is highlighted'''
    web_page = MainPage(driver)
    web_page.open()
    with allure.step('Main page'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    el = driver.find_element_by_xpath("//a[text()='Extras']")
    color1 = el.value_of_css_property("color")
    el.click()
    with allure.step('Extras page'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    el1 = driver.find_element_by_xpath("//a[text()='Extras']")
    color2 = el1.value_of_css_property("color")
    assert color1 != color2



email = "s.kravchenko88@gmail.com"
password = "testtest"

def test_login_to_account(driver, wait):
   '''TC-04 Verify if the registered user can log on the System'''
   web_page = MainPage(driver)
   web_page.open()
   with allure.step('Main page'):
       allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
   web_page.open_login_form(wait)
   web_page.enter_email(email)
   web_page.enter_password(password)
   with allure.step('Login page fulfilled'):
       allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
   web_page.click_eye()
   with allure.step('Password showing'):
       allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
   web_page.submit_login()
   wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='My account']")))
   with allure.step('My account page'):
       allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


def test_icon_platform(driver, wait):
    '''TC-07 Validate if the icons for different Platform are active and navigates correctly'''
    web_page = MainPage(driver)
    web_page.open()
    web_page.click_icon()
    with allure.step('Platform icons'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Second page'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    web_page.find_text(wait)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])



email_test = 'test@mail.ru'

def test_subscribe(driver, wait):
    '''TC-13 Validate if the user can subscribe for newsletter'''
    web_page = MainPage(driver)
    web_page.open()
    with allure.step('Main page'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    web_page.enter_email_for_subscribe(email_test)
    web_page.submit_subscribe()
    with allure.step('Subscribe'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Thanks for subscribing!']")))
    with allure.step('Subcribe confirmation'):
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)

