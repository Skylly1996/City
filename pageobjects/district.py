from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class District_manage(BasePage):
    system_button=(By.CLASS_NAME,"ivu-icon-md-settings")   #点击系统管理
    district_button=(By.XPATH,"//*[@id='app']/div/div[1]/div[1]/div/ul/li[4]/ul/li[2]/span")  #点击区域管理

    district_name=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/input")   #请输入名称
    district_search_button=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/button[1]/span")   #搜索
    district_restart=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/button[2]/span")  #重置

    add2=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/button[3]/span")  #新增子单位
    add2_dis_name=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[1]/div/div/input")   #区域名称
    add2_dis_pin=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[2]/div/div/input")    #拼音简称
    add2_dis_number=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[3]/div/div/input")    #区域编号
    add2_dis_contact=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/input")   #联系人
    add2_dis_promote_tel=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[5]/div/div/input")  #座机电话
    add2_dis_tel=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[6]/div/div/input")  #手机
    add2_dis_chuanzhen=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[7]/div/div/input")  #传真
    add2_dis_mail=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[8]/div/div/input")   #邮编
    add2_dis_address=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[9]/div/div/input")  #地址
    add2_submit=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[3]/div/button[1]/span")    #提交
    add2_close=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[3]/div/button[2]/span")  #关闭

    dis_details=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td[7]/div/div/button[1]/span")  #详情
    dis_details_close=(By.XPATH,"/html/body/div[9]/div[2]/div/div/a/i")


    dis_edit=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td[7]/div/div/button[2]/span")   #编辑
    dis_edit_close=(By.XPATH,"/html/body/div[8]/div[2]/div/div/a/i")

    dis_delete=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td[7]/div/div/button[3]/span")   #删除
    dis_delete_sure=(By.XPATH,"/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]/span")

    def click_district(self):
        self.click(*self.system_button)  #点击系统管理
        self.click(*self.district_button)  #点击区域管理

    def search_name(self,text8):
        self.sendkeys(text8,*self.district_name)  #输入名称
        time.sleep(2)
        self.click(*self.district_search_button)  #搜索
        time.sleep(2)
        self.click(*self.district_restart)   #重置
        time.sleep(2)

    def add_district(self,name,pin,number,contact,promote_tel,tel,chuanzhen,mail,address,):
        self.click(*self.add2)
        self.sendkeys(name,*self.add2_dis_name)
        self.sendkeys(pin,*self.add2_dis_pin)
        self.sendkeys(number,*self.add2_dis_number)
        self.sendkeys(contact,*self.add2_dis_contact)
        self.sendkeys(contact,*self.add2_dis_contact)
        self.sendkeys(promote_tel,*self.add2_dis_promote_tel)
        self.sendkeys(tel,*self.add2_dis_tel)
        self.sendkeys(chuanzhen,*self.add2_dis_chuanzhen)
        self.sendkeys(mail,*self.add2_dis_mail)
        self.sendkeys(address,*self.add2_dis_address)
        self.click(*self.add2_submit)
        self.click(*self.add2_close)

    def details(self):
        self.click(*self.dis_details)
        time.sleep(2)
        self.click(*self.dis_details_close)

    def edit(self):
        self.click(*self.dis_edit)
        time.sleep(2)
        self.click(*self.dis_edit_close)

    def delete(self):
        self.click(*self.dis_delete)
        time.sleep(2)
        self.click(*self.dis_delete_sure)