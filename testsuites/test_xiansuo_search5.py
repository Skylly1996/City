import unittest
from framework2.logger import Logger
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.city_xiansuo_page import City_xiansuo_page

logger=Logger(logger="BasePage").getlog()
class Xiansuo_Search(BaseTestCase):

    def test_xiansuo_search(self):
        # 先登录
        login_page = CityPage(self.driver)
        login_page.login1('18210034706', "123456")

        xiansuo_page = City_xiansuo_page(self.driver)
        xiansuo_page.xuncha_wind()
        xiansuo_page.search_xiansuo()
        xiansuo_page.resetting_xiansuo()
        xiansuo_page.details_xiansuo()



if __name__ == '__main__':
    unittest.main(verbosity=2)