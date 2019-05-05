from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


# 进入巡查管理
class System_juese_management(BasePage):

    def juese_wind(self):
        systement=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[4]/div/span')
        juese=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[4]/ul/li[3]/span')
        self.change_window()
        self.click(*systement)
        self.click(*juese)


    # 点击详情查看角色管理
    def details_juese(self):
        details_js = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button/span')
        jsdetails_close=(By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/button/span')
        # self.change_window()
        time.sleep(1)
        self.click(*details_js)
        time.sleep(2)
        self.click(*jsdetails_close)


