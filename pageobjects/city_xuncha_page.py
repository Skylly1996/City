from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


# 进入巡查管理
class City_xuncha_page(BasePage):

    # def xuncha_wind(self):
    #     menu_name = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/li[2]/span')
    #     self.change_window()
    #     self.click(*menu_name)

    # 新增巡查记录有无违规
    def add_xuncha_record(self):

        add_record = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/button[3]/span')
        # 巡查记录框
        weigui= (By.CSS_SELECTOR, '.ivu-form-item-content label ')
        leixing_down=(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/div/i')
        changsuo_leixing = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/ul[2]/li[1]')

        changsuo_kuang = (By.XPATH,'//*[@id="placeName"]/input')
        changsuo_name = (By.XPATH, '/html/body/div[12]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/div/button/span')
        text_down=(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/i')
        xuncha_text = (By.XPATH, '/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[2]/ul[2]/li')
        # submit = (By.XPATH, '/html/body/div[9]/div[2]/div/div/div[3]/div/button[1]/span')
        close=(By.XPATH,"/html/body/div[9]/div[2]/div/div/a/i")
        # queren = (By.XPATH, '/html/body/div[17]/div[2]/div/div/div/div/div[3]/button[2]/span')

        self.change_window()
        self.click(*add_record)
        time.sleep(2)
        self.get_windows_img()
        self.click(*weigui)

        self.click(*leixing_down)
        # time.sleep(2)
        self.click(*changsuo_leixing)
        time.sleep(2)
        self.click(*changsuo_kuang)
        # time.sleep(2)
        self.click(*changsuo_name)
        time.sleep(2)
        self.click(*text_down)
        # time.sleep(2)
        self.click(*xuncha_text)

        self.get_windows_img()
        self.click(*close)
        # time.sleep(2)
        # self.click(*queren)

    # 查询完后点击重置，页面跳转到巡查首页
    xuncha_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[2]/span')#进入巡查管理模块
    xiangqing_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div/div/button/span')#详情按钮
    xiangqingExit_loc=(By.XPATH,'/html/body/div[10]/div[2]/div/div/a/i')#退出详情页

    search1_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[6]/input')#搜索巡查人框
    search2_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/button[1]/span')#搜索按钮
    chongzhi_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/button[2]/span')#重置

    def xunCha(self):#进入管理中心
        self.click(*self.xuncha_loc)

    def xiangQing(self):#点击查看巡查记录详情并退出其界面
        self.click(*self.xiangqing_loc)
        self.get_windows_img()
        time.sleep(3)
        self.click(*self.xiangqingExit_loc)

    def search_xunchaPeople(self,txt):
        self.sendkeys(txt,*self.search1_loc)
        self.click(*self.search2_loc)
        self.get_windows_img()
        time.sleep(2)
        self.click(*self.chongzhi_loc)
        self.get_windows_img()
        time.sleep(3)


