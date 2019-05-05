import time,unittest,xlrd
from testsuites.base_testcase import BaseTestCase
from pageobjects.city_login import CityPage
from ddt import ddt,data,unpack
@ddt
class Test_Login(BaseTestCase):
    @unpack
    def test_Login(self):
        test_login = CityPage(self.driver)
        print('la5')
        data = xlrd.open_workbook('E:/python-webUI-DISCUZ/data/login.xlsx')
        table = data.sheet_by_name('Sheet1')
        text1 = test_login.login1(int(table.row_values(1)[0]), int(table.row_values(1)[1]))
        try:
            self.assertEqual(text1, '首页', msg=text1)
            print('断言结果:登录成功')
        except:
            print('断言结果:用户名错误')
        text2 = test_login.login1(int(table.row_values(2)[0]), int(table.row_values(2)[1]))
        try:
            self.assertEqual(text2, '首页', msg=text2)
            print('断言结果:登录成功')
        except:
            print('断言结果:密码错误')
        text3 = test_login.login1(int(table.row_values(3)[0]), int(table.row_values(3)[1]))
        try:
            self.assertEqual(text3, '首页', msg=text3)
            print('断言结果:登录成功')
        except:
            print('断言结果:用户名或密码错误')
if __name__=='__main__':
    unittest.main()