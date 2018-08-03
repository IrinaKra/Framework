import allure
from allure.constants import AttachmentType


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
