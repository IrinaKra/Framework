import os

os.system('rmdir reports')
os.system('py.test --alluredir reports Education\Lesson2.py')
os.system('allure serve reports --clean')