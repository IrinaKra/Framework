import allure
from allure.constants import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PlanPage:

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def open(self):
       self.driver.get('https://www.vpnunlimitedapp.com/en/pricingb')
       self.driver.set_window_size(1920, 1080)
       with allure.step('Pricing page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
       return self

   def plan(self):
       self.driver.find_element_by_xpath("//a[@class='prices_cnt--item price-month ']").click()
       self.wait.until(
           EC.presence_of_element_located((By.XPATH, "//div[@class='pricing_title_in_header']/descendant::h2")))
       with allure.step('Login form'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
       return self

   def change_plan(self):
       self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Change plan')]"))).click()

   def element_not_visible(self):
       element = self.driver.find_element_by_xpath("//div[@class='pricing_title_in_header']/descendant::h2")
       self.driver.refresh()
       self.wait.until(EC.staleness_of(element))
       with allure.step('Plan page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)