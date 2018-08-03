import allure
from allure.constants import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class VideoPage:

   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait

   def open_video(self):
       self.driver.find_element_by_xpath("//div[@class='pulse2']").click()
       self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='videoWrapper']/descendant::video")))
       with allure.step('Video page'):
           allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
       return self


