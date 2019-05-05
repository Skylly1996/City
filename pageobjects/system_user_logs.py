from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


# 进入巡查管理
class System_user_logs(BasePage):

    def logs_wind(self):
        systement=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[4]/div/span')
        user_logs=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[4]/ul/li[4]/i')
        self.change_window()
        self.click(*systement)
        self.click(*user_logs)

    # 根据输入条件查询有无违规
    def search_logs(self,a,b):
        gongneng = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/input')
        fangfa = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/input')

        log_record = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/button[1]')

        self.change_window()
        time.sleep(2)
        self.sendkeys(a,*gongneng)
        time.sleep(2)
        self.sendkeys(b,*fangfa)

        time.sleep(2)
        self.click(*log_record)

    # 查询完后点击重置，页面跳转到巡查首页
    def resetting_logs(self):
        resetting_log = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/button[2]')
        time.sleep(5)
        self.click(*resetting_log)


    # 点击详情查看角色管理
    def details_logs(self):
        details_log = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/button')
        logs_close=(By.XPATH,'/html/body/div[8]/div[2]/div/div/div[3]/div/button/span')

        time.sleep(1)
        self.click(*details_log)
        time.sleep(2)
        self.click(*logs_close)


