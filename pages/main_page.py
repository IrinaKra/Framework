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
