import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.city_exit import City_exit
from pageobjects.place_type import City_management
from framework2.util import Util
import time

class CityLogin(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = CityPage(self.driver)
        home_page1.login1("18210034706","123456")  #用户登录系统

        home_page3=City_management(self.driver)
        home_page3.manage1()      #进入场所类型管理

        for i in range(0,5):
            util=Util()
            dic=util.read_excel("E:/python-webUI-DISCUZ/data/example.xlsx","Sheet1")
            a=dic[i]["类型名称"]
            b=int(dic[i]["类型编码"])
            home_page3.type_manage(a,b)  #新增场所类型

        home_page3.edit("httttt","981289")   #编辑场所类型
        time.sleep(5)

        home_page3.delete()   #删除场所类型
        time.sleep(2)

        home_page3.add_weifa("12345236","dsxca","jdskhfja")

        home_page2=City_exit(self.driver)
        time.sleep(2)
        home_page2.exit1()   #用户退出
        time.sleep(5)

if __name__=='__main__':
    unittest.main()

