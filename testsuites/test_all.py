import sys
sys.path.append('E:\python-webUI-City')
import unittest
import HTMLTestRunner
import os
current_path=os.path.abspath(__file__)
a_path=os.path.dirname(current_path)
b_path=os.path.dirname(a_path)
from framework2.logger import Logger
from testsuites.test_login import Test_Login
from testsuites.test_city1 import CityLogin
from  testsuites.test_xinxi_search3 import Cityxinxi
from testsuites.test_xuncha_search4 import Xuncha_Search
from testsuites.test_xiansuo_search5 import Xiansuo_Search
from testsuites.test_user_manage import User_manage
from testsuites.test_district_manage import Dis1_manage
from testsuites.test_juese_search8 import Juese_Search
from testsuites.test_log_search9 import Log_Search


file_path=os.path.dirname(os.path.abspath("."))+"/test_report"

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Logger))

suite.addTest(unittest.makeSuite(Test_Login))
suite.addTest(unittest.makeSuite(CityLogin))
suite.addTest(unittest.makeSuite(Cityxinxi))
suite.addTest(unittest.makeSuite(Xuncha_Search))
suite.addTest(unittest.makeSuite(Xiansuo_Search))
suite.addTest(unittest.makeSuite(User_manage))
suite.addTest(unittest.makeSuite(Dis1_manage))
suite.addTest(unittest.makeSuite(Juese_Search))
suite.addTest(unittest.makeSuite(Log_Search))

if __name__=="__main__":
    html_report=file_path+r"\report.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="关于City的测试报告")
    runner.run(suite)
