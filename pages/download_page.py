from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from allure.constants import AttachmentType


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