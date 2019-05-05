import unittest
from framework2.logger import Logger
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.system_user_logs import System_user_logs

logger=Logger(logger="BasePage").getlog()
class Log_Search(BaseTestCase):
    def test_log_search(self):
        # 先登录
        home_page1 = CityPage(self.driver)
        home_page1.login1("18210034706","123456")

        log_page = System_user_logs(self.driver)
        log_page.logs_wind()

        log_page.search_logs('登录','查询')
        log_page.details_logs()

        log_page.resetting_logs()


if __name__ == '__main__':
    unittest.main(verbosity=2)