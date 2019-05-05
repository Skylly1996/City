import unittest
from framework2.logger import Logger
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.system_juese_mangement import System_juese_management

logger=Logger(logger="BasePage").getlog()
class Juese_Search(BaseTestCase):
    def test_juese_search(self):
        # 先登录
        login_page = CityPage(self.driver)
        login_page.login1('18210034706', "123456")

        juese_page = System_juese_management(self.driver)
        juese_page.juese_wind()
        juese_page.details_juese()




if __name__ == '__main__':
    unittest.main(verbosity=2)