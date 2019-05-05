from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class City_information(BasePage):
    place_button=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[1]/div/span')    #点击场所管理
    information_button=(By.XPATH,"//*[@id='app']/div/div[1]/div[1]/div/ul/li[1]/ul/li[2]/span")  #点击场所信息管理

    add_type_information=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/button[4]/span")  #新增场所信息

    add_type=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/div/i")   #场所类型按钮
    add_type_place=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/div/div[2]/ul[2]/li[2]")  #场所类型
    add_type_name=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div/input")  #请输入场所名称
    add_contact=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div/div/input")  #日常联系人
    add_contact_tel=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div/div/input")   #日常联系人电话号码
    add_involv1=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[7]/div/div[1]/div[1]/div/i")  #第一个请选择
    add_involv1_1=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[7]/div/div[1]/div[2]/ul[2]/li[1]")   #东城区
    add_involv2=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[7]/div/div[2]/div[1]/div/i")   #第二个请选择
    add_involv2_2=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[7]/div/div[2]/div[2]/ul[2]/li[3]")  #沙河
    add_involv3=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[7]/div/div[3]/div[1]/div/i")  #第三个选择
    add_involv3_3=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div[7]/div/div[3]/div[2]/ul[2]/li")  #高效
    add_sumit=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[3]/div/button[1]/span")  #提交
    add_close=(By.XPATH,"/html/body/div[13]/div[2]/div/div/div[3]/div/button[2]/span")  #关闭

    def add_information(self):
        self.click(*self.place_button)
        time.sleep(5)
        self.click(*self.information_button)

    def add(self,name,contact,contact_tel):
        self.click(*self.add_type_information)
        time.sleep(2)
        self.click(*self.add_type)
        time.sleep(2)
        self.click(*self.add_type_place)
        time.sleep(2)
        self.sendkeys(name,*self.add_type_name)
        self.sendkeys(contact,*self.add_contact)
        self.sendkeys(contact_tel,*self.add_contact_tel)
        self.click(*self.add_involv1)
        self.click(*self.add_involv1_1)
        self.click(*self.add_involv2)
        self.click(*self.add_involv2_2)
        self.click(*self.add_involv3)
        self.click(*self.add_involv3_3)
        self.click(*self.add_sumit)
        self.click(*self.add_close)


