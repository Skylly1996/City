from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


# 进入巡查管理
class City_xiansuo_page(BasePage):
    # 点击巡查管理
    def xuncha_wind(self):
        menu_name = (By.CSS_SELECTOR, '.ivu-menu-vertical .ivu-menu-item .ivu-icon-ios-color-wand')

        self.change_window()
        self.click(*menu_name)

    # 审核违规记录是否有效
    def auditing_xuncha_record(self):

        auditing_xs = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div/div/button[2]/span')

        self.click(*auditing_xs)
        time.sleep(2)
        self.get_windows_img()

     # 根据输入条件查询违规状态
    def search_xiansuo(self):
        qyu_down=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/i')
        quyu = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[9]')
        jiedao_down=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/i')
        jiedao = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/ul[2]/li[1]')
        shequ_down = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[3]/div[1]/div/i')
        shequ = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[3]/div[2]/ul[2]/li')
        # quyu = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[9]')

        search_xs = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/button[1]')
        self.change_window()
        time.sleep(2)
        self.click(*qyu_down)
        time.sleep(2)
        self.click(*quyu)
        self.click(*jiedao_down)
        time.sleep(2)
        self.click(*jiedao)
        self.click(*shequ_down)
        time.sleep(2)
        self.click(*shequ)
        self.click(*search_xs)
    # 查询完后点击重置，页面跳转到线索首页
    def resetting_xiansuo(self):
        resetting_xs = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/button[2]/span')

        self.click(*resetting_xs)

    # 点击详情查看所属区域的巡查人员有无发现违规
    def details_xiansuo(self):
        details_xs = (By.CSS_SELECTOR, '.ivu-table-column-center .ivu-btn-small')

        time.sleep(1)
        self.click(*details_xs)


