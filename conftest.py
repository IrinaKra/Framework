import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.yield_fixture(scope="session")
def driver():
    _driver = webdriver.Chrome('D:\\Users\\j\\PycharmProjects\\KeepSolid\\chromedriver')
    return _driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait

@pytest.fixture(scope="session", autouse=True)
def stop(request, driver):
    def fin():
        driver.quit()
    request.addfinalizer(fin)
