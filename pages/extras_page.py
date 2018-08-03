import allure
from allure.constants import AttachmentType


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