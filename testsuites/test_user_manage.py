import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.system import System_manage
from pageobjects.city_exit import City_exit
import time


class User_manage(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = CityPage(self.driver)
        home_page1.login1('18210034706','123456')  #登录

        home_page2=System_manage(self.driver)
        home_page2.click_user()    #点击用户管理

        home_page2.search_name("n")
        home_page2.search_tel(15935157073)

        home_page2.add_user("狗1子","15935156048","010-12345678","3032988695@qq.com","1朝阳区")

        home_page2.user_particulars()
        time.sleep(2)
        home_page2.user_edit()
        time.sleep(2)
        home_page2.user_stop()
        time.sleep(2)
        home_page2.user_reset()

        home_page2.left_search()

        home_page2=City_exit(self.driver)
        time.sleep(2)
        home_page2.exit1()   #用户退出
        time.sleep(5)

if __name__=='__main__':
    unittest.main()