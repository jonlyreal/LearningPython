"""
Author ：SunJie
复制第三课的代码，修改几个名字
"""
from selenium import webdriver #下载了selenium之后，我可以把selenium导入进来
import unittest


class Mytest(unittest.TestCase):  # 写个类，继承unnitest.Testcase
    """
    生命周期按照下列方式排序
    setUp
    testOne
    teardown
    ----------
    setUp
    testTwo
    teardown
    """

    def setUp(self):
        self.my_window = webdriver.Chrome()  # 申明了一个chrome浏览器
        self.my_window.get("http://192.168.14.103:8083/osf-pvs-mock/ftl/requestApplyOsf.jsp")  # 用浏览器打开测试的网站

    def tearDown(self):
        self.my_window.close()  # 关闭浏览器

    def test_a_one_copy(self):
        membercode = self.my_window.find_element_by_name('membercode')
        membercode.clear()
        membercode.send_keys('123456')


if __name__ == '__main__':
    unittest.main()