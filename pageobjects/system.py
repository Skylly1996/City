from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class System_manage(BasePage):
    system_button=(By.CLASS_NAME,"ivu-icon-md-settings")   #点击系统管理
    user_button=(By.CLASS_NAME,"ivu-icon-md-person")    #点击用户管理

    please_name=(By.CLASS_NAME,("ivu-input-default"))  #请输入用户姓名
    search_button1=(By.CSS_SELECTOR,".search-top button:nth-child(3)")   #搜索

    please_tel=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/input")  #请输入手机号

    reset_button=(By.CSS_SELECTOR,".search-top button:nth-child(4)")  #重置

    add1=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/button[3]/span")   #新增用户
    add1_name=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[1]/div/div/input")   #姓名
    add1_tel=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[2]/div/div/input")   #手机
    add1_special_tel=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[3]/div/div/input")   #座机号
    add1_mail=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/input") #电子邮箱
    add1_address=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[5]/div/div/input")  #地址
    add1_role_button=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[6]/div/div/div[1]/div/i")   #角色下拉框
    add1_zong=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[6]/div/div/div[2]/ul[2]/li[1]")
    add1_xun=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[6]/div/div/div[2]/ul[2]/li[2]")
    add1_fei=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[2]/form/div[6]/div/div/div[2]/ul[2]/li[3]")
    add1_submit=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[3]/div/button[1]/span")  #提交
    add1_close=(By.XPATH,"/html/body/div[8]/div[2]/div/div/div[3]/div/button[2]/span")   #关闭


    particulars=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[1]/span")  #详情
    p_close=(By.XPATH,"/html/body/div[9]/div[2]/div/div/a/i")

    edit=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[2]/span")  #编辑
    e_close=(By.XPATH,"/html/body/div[8]/div[2]/div/div/a/i")

    stop=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[3]/span")  #停用
    s_sure=(By.XPATH,"/html/body/div[10]/div[2]/div/div/div/div/div[3]/button[2]/span")

    reset=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[4]/span")  #重置密码子

    beijing=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/ul/li/span[1]/i")   #点击北京
    dongcheng=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/ul/li/ul[1]/li/span[1]/i")  #东城区
    dongjie=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/ul/li/ul[1]/li/ul[1]/li/span[1]/i')  #东华街道
    dongshequ=(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/ul/li/ul[1]/li/ul[1]/li/ul[1]/li/span[2]")   #东华门社区



    def click_user(self):
        self.click(*self.system_button)  #点击系统管理
        self.click(*self.user_button)  #点击用户管理

    def search_name(self,text3):
        self.sendkeys(text3,*self.please_name)    #请输入用户姓名
        self.click(*self.search_button1)   #搜索
        time.sleep(2)
        self.click(*self.reset_button)

    def search_tel(self,text4):
        self.sendkeys(text4,*self.please_tel)  #请输入手机号
        self.click(*self.search_button1)   #搜索
        time.sleep(2)
        self.click(*self.reset_button)

    def add_user(self,name,tel,special,mail,address):
        self.click(*self.add1)
        self.sendkeys(name,*self.add1_name)
        self.sendkeys(tel,*self.add1_tel)
        self.sendkeys(special,*self.add1_special_tel)
        self.sendkeys(mail,*self.add1_mail)
        self.sendkeys(address,*self.add1_address)

        self.click(*self.add1_role_button)
        self.click(*self.add1_zong)
        self.click(*self.add1_xun)
        self.click(*self.add1_fei)

        self.click(*self.add1_submit)
        self.click(*self.add1_close)

    def user_particulars(self):
        self.click(*self.particulars)
        self.click(*self.p_close)

    def user_edit(self):
        self.click(*self.edit)
        self.click(*self.e_close)

    def user_stop(self):
        self.click(*self.stop)
        self.click(*self.s_sure)

    def user_reset(self):
        self.click(*self.reset)

    def left_search(self):
        self.click(*self.beijing)
        self.click(*self.dongcheng)
        self.click(*self.dongjie)
        self.click(*self.dongshequ)



