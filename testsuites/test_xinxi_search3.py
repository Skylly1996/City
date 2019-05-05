import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from pageobjects.city_chuangsuo_xinxi import City_xinxi
from framework2.util import Util
import time

class Cityxinxi(BaseTestCase):
    def test_xinxi_search(self):
        login_page = CityPage(self.driver)
        login_page.login1("18210034706","123456")  #用户登录系统

        xinxi_page=City_xinxi(self.driver)
        xinxi_page.xinxi_wind()   #进入场所类型管理

        xinxi_page.add_leixing('cccc','15935615697')
        xinxi_page.xinxi_xiangqing()
        xinxi_page.edit_xinxi()
        xinxi_page.delete_changsuo()
        xinxi_page.xuncha_jilu()


if __name__=='__main__':
    unittest.main()
