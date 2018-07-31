from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from allure.contains import AttachmentType


def test_company_logo(driver, wait):
    '''TC-01 The Company Logo is active and works correctly'''
    driver.set_window_size(1920, 1080) # if the browser window is not fullscreen, the header menu is not available
    driver.get('https://www.vpnunlimitedapp.com/en')
    with allure.step('First page'):
        allure.attach('screnshot', driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    el1 = driver.find_element_by_xpath("//img[@class='sm-hide']")
    el1.click()
    el2 = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']/descendant::a[contains(text(),'Pricing')]")
    el2.click()
    with allure.step('Second page'):
        allure.attach.file('screnshot', driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@class='sm-hide']"))).click()
    assert driver.current_url == 'https://www.vpnunlimitedapp.com/en'


def test_active_link(driver):
    '''TC-02 Verify if the header part is always visible and active link is highlighted'''
    driver.set_window_size(1920, 1080)
    driver.get('https://www.vpnunlimitedapp.com/en')
    el = driver.find_element_by_xpath("//a[text()='Extras']")
    color1 = el.value_of_css_property("color")
    el.click()
    el1 = driver.find_element_by_xpath("//a[text()='Extras']")
    color2 = el1.value_of_css_property("color")
    assert color1 != color2


def test_sign_in(driver, wait):
    '''TC-04 Verify if the registered user can log on the System'''
    driver.set_window_size(1920, 1080)
    driver.get('https://www.vpnunlimitedapp.com/en')
    el1 = driver.find_element_by_xpath("//a[text()='Sign In']")
    el1.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-popup--container']")))
    email = driver.find_element_by_xpath("//input[@name='login']")
    email.send_keys("s.kravchenko88@gmail.com")
    password = driver.find_element_by_xpath("//input[@name='password']")
    password.send_keys("testtest")
    eye = driver.find_element_by_xpath("//span[@class='icon-font-eye']")
    eye.click()
    driver.find_element_by_xpath("//button[@type='submit']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='My account']")))


def test_icon_platform(driver, wait):
    '''TC-07 Validate if the icons for different Platform are active and navigates correctly'''
    driver.get('https://www.vpnunlimitedapp.com/en')
    driver.find_element_by_xpath("//img[@alt='VPN Unlimited for macOS']").click()
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.presence_of_element_located((By.XPATH,"//h2[text()=' for macOS']")))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_xpath("//img[@alt='VPN Unlimited for iOS']").click()
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.presence_of_element_located((By.XPATH,"//h2[text()=' for iOS']")))


def test_subscribe(driver, wait):
    '''TC-13 Validate if the user can subscribe for newsletter'''
    driver.get('https://www.vpnunlimitedapp.com/en')
    email = driver.find_element_by_xpath("//input[@name='email']")
    email.send_keys("test@mail.ru")
    driver.find_element_by_xpath("//label[@class='footer_input_btn_label']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-popup--content']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Thanks for subscribing!']")))

#  --alluredir=reports/ --junitxml=report.xml
