import xlrd
import unittest
# from framework2.logger import Logger

class Search(unittest.TestCase):
    data=xlrd.open_workbook('example.xlsx')  #Excel表路径、名称
    table=data.sheet_by_name('Sheet1')    #sheet页名称

    nrows=table.row_values(2)  #获取表格第几行数据，0是第一行
    name=nrows[0]
    code=nrows[1]
    print(name,code)

if __name__ == "__main__":
    unittest.main()
