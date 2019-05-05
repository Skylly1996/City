from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class City_exit(BasePage):
    exit_login = (By.CLASS_NAME, 'ivu-icon-md-arrow-dropdown')  # 退出网页的登录登录
    eiit_button=(By.CLASS_NAME,'ivu-dropdown-item')
    def exit1(self):
        self.click(*self.exit_login)
        self.click(*self.eiit_button)