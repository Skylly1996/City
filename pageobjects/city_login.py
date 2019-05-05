from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

# 继承BasePage类
class CityPage(BasePage):
    loginName_loc=(By.NAME,'userName')
    loginPwd_loc=(By.NAME,'password')
    loginClick_loc=(By.ID,'loginBtn')

    def login1(self,username,pwd):
        self.sendkeys(username, *self.loginName_loc)
        self.sendkeys(pwd, *self.loginPwd_loc)
        self.click(*self.loginClick_loc)
        self.get_windows_img()
