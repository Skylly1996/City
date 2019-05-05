import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.city_exit import City_exit
from pageobjects.place_information import  City_information
import time

class CityLogin(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = CityPage(self.driver)
        home_page1.login1('18210034706','123456')  #登录

        home_page2=City_information(self.driver)
        home_page2.add_information()
        home_page2.add("nyx","张珊","15935157073")

        home_page2=City_exit(self.driver)
        time.sleep(2)
        home_page2.exit1()   #用户退出
        time.sleep(5)
if __name__=='__main__':
    unittest.main()
