from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from allure.constants import AttachmentType


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