import unittest
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class City_xinxi(BasePage):
    # 点击场所管理,点击场所信息管理
    def xinxi_wind(self):
        changsuo_loc = (By.CSS_SELECTOR, ".ivu-menu-submenu-title")
        changsuoxinxi_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/li[1]/ul/li[2]/span')
        time.sleep(2)
        self.change_window()
        self.click(*changsuo_loc)
        self.click(*changsuoxinxi_loc)

    # 新增场所信息
    def add_leixing(self, leixing_name, leixing_num):
        xinxi_add_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/button[4]/span')
        changsuo_xinxi_down = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/div/i")
        changsuo_xinxi_name = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/div/div[2]/ul[2]/li[1]")
        changsuo_name = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div/input")
        richang_name = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div/div/input")
        telephone = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div/div/input")
        changsuo_suoshu_down = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[7]/div/div[1]/div[1]/div/i")
        quyu = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[7]/div/div[1]/div[2]/ul[2]/li[1]")
        jiedao_down = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[7]/div/div[2]/div[1]/div/i")
        jiedao = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div/input")
        shequ_down = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[7]/div/div[3]/div[1]/div/i")
        shequ = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div/input")

        # 提交
        submit = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[3]/div/button[1]/span")
        close = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[3]/div/button[2]/span")
        # 点击新增场所类型
        self.click(*xinxi_add_loc)
        self.click(*changsuo_xinxi_down)
        self.click(*changsuo_xinxi_name)
        self.sendkeys(leixing_name, *changsuo_name)
        self.sendkeys(leixing_num, *richang_name)
        self.sendkeys(leixing_num, *telephone)
        self.click(*changsuo_suoshu_down)
        self.click(*quyu)
        self.click(*jiedao_down)
        self.click(*jiedao)
        self.click(*shequ_down)
        self.click(*shequ)
        time.sleep(1)
        # 点击提交按钮
        self.click(*submit)
        time.sleep(1)
        # self.click(*close)

    # 编辑场所信息
    def edit_xinxi(self):
        edit= (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/button[2]/span')
        self.click(*edit)
    # 删除场所信息
    def delete_changsuo(self):
        zhuxiao = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/button[3]/span')
        self.click(*zhuxiao)
    # 场所信息详情
    def xinxi_xiangqing(self):
        xiangqing= (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/button[1]')

        self.click(*xiangqing)
    # 巡查记录
    def xuncha_jilu(self):
        jilu=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/button[4]/span')

        self.click(*jilu)





