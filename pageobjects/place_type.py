from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class City_management(BasePage):
    place_button=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[1]/div/span')    #点击场所管理
    type_button=(By.XPATH,"//div/ul/li[1]/ul/li[1]/span")  #点击场所类型管理
    add_type_button2=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/ul/li/span[2]/span[2]/button/span")

    type_name_input=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input")  #场所类型名称
    type_coding_input=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input")    #类型编码
    type_manage1_button=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/button[1]/span")
    type_manage2_button=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/button[2]/span")

    type_delete=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/ul/li/ul[1]/li/span[2]/span[2]/button[2]")
    type_delete_ensure=(By.XPATH,"/html/body/div[42]/div[2]/div/div/div/div/div[3]/button[2]/span")
    type_delete_cancel=(By.XPATH,"/html/body/div[42]/div[2]/div/div/div/div/div[3]/button[1]/span")

    type_edit=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/ul/li/ul[2]/li/span[2]/span[2]/button[1]/i")
    type_name1=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[2]/form/div[1]/div/div/input")  #编辑类型名称
    type_coding_input2=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[2]/form/div[2]/div/div/input")
    type_submit1=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/button[1]/span")

    add2_illegal=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/button/span") #新增违法行为
    add2_anli=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[1]/div/div/input")  #案由摘要
    add2_shuoming=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[2]/div/div/textarea")  #案由说明
    add2_clause=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[3]/div/div/textarea")   #违法条款
    add2_sumit=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[3]/div/button[1]/span")  #提交
    add2_close=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[3]/div/button[2]/span")  #关闭


    def manage1(self):#进入管理中心
        self.click(*self.place_button)
        self.click(*self.type_button)
        self.get_windows_img()

    def type_manage(self,text1,text2):
        self.click(*self.add_type_button2)  #新增场所类型
        self.sendkeys(text1, *self.type_name_input)
        self.click(*self.type_coding_input)
        self.sendkeys(text2, *self.type_coding_input)
        self.click(*self.type_manage1_button)
        self.click(*self.type_manage2_button)

    def delete(self):
        self.click(*self.type_delete)
        self.click(*self.type_delete_ensure)
        self.click(*self.type_delete_cancel)

    def edit(self,text3,text4):
        self.click(*self.type_edit)
        time.sleep(2)
        self.clear(*self.type_name1)
        self.sendkeys(text3,*self.type_name1)
        self.clear(*self.type_coding_input2)
        self.sendkeys(text4,*self.type_coding_input2)
        self.click(*self.type_submit1)

    def add_weifa(self,anli,shuoming,clause):
        self.click(*self.add2_illegal)
        self.sendkeys(anli,*self.add2_anli)
        self.sendkeys(shuoming,*self.add2_shuoming)
        self.sendkeys(clause,*self.add2_clause)
        self.click(*self.add2_sumit)

    def add_detail(self):
        pass








