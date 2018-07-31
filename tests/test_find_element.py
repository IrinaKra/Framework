from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_second(driver, wait):
    driver.get('https://www.vpnunlimitedapp.com/en/pricing')
    el1 = driver.find_element_by_xpath("//a[@class='prices_cnt--item']")
    el1.click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='pricing_title_in_header']/descendant::h2")))
    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Change plan')]"))).click()
    el2 = driver.find_element_by_xpath("//div[@class='pricing_title_in_header']/descendant::h2")
    driver.refresh()
    wait.until(EC.staleness_of(el2))

def test_first(driver, wait):
    driver.get('https://www.vpnunlimitedapp.com/en')
    el = driver.find_element_by_xpath("//div[@class='pulse2']")
    el.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='videoWrapper']/descendant::video")))

