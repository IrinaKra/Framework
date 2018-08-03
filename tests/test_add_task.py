from pages.plan_page import PlanPage
from pages.main_page import MainPage
from pages.video_page import VideoPage


def test_element_not_visible(driver, wait):
    web_page = PlanPage(driver, wait)
    web_page.open()
    web_page.plan()
    web_page.change_plan()
    web_page.element_not_visible()


def test_video(driver, wait):
    web_page = MainPage(driver, wait)
    video_page = VideoPage(driver, wait)
    web_page.open()
    video_page.open_video()

