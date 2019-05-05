import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.district import District_manage
from pageobjects.city_exit import City_exit
from pageobjects.city_exit import City_exit
import time


class Dis1_manage(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = CityPage(self.driver)
        home_page1.login1('18210034706','123456')  #登录

        home_page2=District_manage(self.driver)
        home_page2.click_district()  #区域管理

        home_page2.search_name("东城区")

        home_page2.add_district("东边的城区","dongbiande","4545","牛玉香","010-12345678","15935157073","12345","100000","你猜")
        time.sleep(5)

        home_page2.details()
        time.sleep(5)

        home_page2.edit()
        time.sleep(5)

        home_page2.delete()


        home_page2=City_exit(self.driver)
        time.sleep(2)
        home_page2.exit1()   #用户退出
if __name__=="__main__":
    unittest.main()

