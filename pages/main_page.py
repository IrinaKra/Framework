from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from allure.constants import AttachmentType


class MainPage:

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def open(self):
       self.driver.get('https://www.vpnunlimitedapp.com/en')
       self.driver.set_window_size(1920, 1080)
       with allure.step('Main page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
       return self


class PricingPage:

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def open(self):
       self.driver.find_element_by_xpath("//a[contains(text(),'Pricing')]").click()
       with allure.step('Pricing page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

   def company_logo(self):
       self.driver.find_element_by_xpath("//img[@class='sm-hide']").click()
       with allure.step('Main page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)


class ExtrasPage:

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def open(self):
       self.driver.find_element_by_xpath("//a[text()='Extras']").click()
       with allure.step('Extras'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

   def link_color(self):
       color = self.driver.find_element_by_xpath("//a[text()='Extras']").value_of_css_property("color")
       return color


class LoginPage:

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def open(self):
       self.driver.find_element_by_xpath("//a[text()='Sign In']").click()
       self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-popup--container']")))
       return self

   def enter_email(self, email):
       self.driver.find_element_by_xpath("//input[@name='login']").send_keys(email)
       return self

   def enter_password(self, password):
       self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
       with allure.step('Login page fulfilled'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
       return self

   def click_eye(self):
       self.driver.find_element_by_xpath("//span[@class='icon-font-eye']").click()
       with allure.step('Password showing'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

   def submit_login(self):
       self.driver.find_element_by_xpath("//button[@type='submit']").click()

   def login_confirm(self):
       self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='My account']")))
       with allure.step('My account page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)


class DownloadPage:

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def icon(self):
       self.driver.find_element_by_xpath("//img[@alt='VPN Unlimited for macOS']").click()

   def next_tab(self):
       self.driver.switch_to.window(self.driver.window_handles[1])

   def text(self):
       self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()=' for macOS']")))
       with allure.step('Platform page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
       self.driver.close()
       return self

   def previous_tab(self):
       self.driver.switch_to.window(self.driver.window_handles[0])


class SubscribePage():

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def enter_email(self, email_test):
       self.driver.find_element_by_xpath("//input[@name='email']").send_keys(email_test)
       return self

   def submit_subscribe(self):
       self.driver.find_element_by_xpath("//label[@class='footer_input_btn_label']").click()
       with allure.step('Subscribe'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
       return self

   def subcribe_confirm(self):
       self.wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Thanks for subscribing!']")))
       with allure.step('Subcribe confirmation'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)