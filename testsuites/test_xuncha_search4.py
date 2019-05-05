import unittest
from framework2.logger import Logger
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.city_xuncha_page import City_xuncha_page

logger=Logger(logger="BasePage").getlog()
class Xuncha_Search(BaseTestCase):
    def test_xuncha_search(self):
        # 先登录
        login_page = CityPage(self.driver)
        login_page.login1('18210034706', "123456")

        home_page2=City_xuncha_page(self.driver)
        home_page2.xunCha()
        home_page2.xiangQing()
        home_page2.search_xunchaPeople('11')
        home_page2.add_xuncha_record()

        # try:
        #     xuncha=xuncha_page.add_xuncha_record('ccccc')
        #     self.assertEqual(xuncha, '18210034706', msg=xuncha)
        #     logger.info('实际值与期望值一致')
        #     print("实际值与期望值一致")
        # except:
        #     logger.error('实际值与期望值不一致')
        #     print("实际值与期望值不一致")

if __name__ == '__main__':
    unittest.main(verbosity=2)