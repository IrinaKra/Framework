from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from allure.constants import AttachmentType


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