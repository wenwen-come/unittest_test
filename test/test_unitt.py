#coding:utf-8
import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, unpack    #数据驱动

#Unitest类，必须继承与Case类
@ddt
class UnitDemo(unittest.TestCase):
    #前置条件
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("setup Function")

    #后置条件
    @classmethod
    def tearDown(self):
        self.driver.quit()
        print('tearadown Function')


    #测试用例
    #@data('python', 'java', 'robotframework')
    @data(('http://baidu.com','python'),('http://baidu.com', 'java'), ('http://baidu.com','robotframework'))
    @unpack
    def test_a(self, url, text):
        driver = self.driver
        driver.get(url)
        driver.find_element_by_id('kw').send_keys(text)
        driver.find_element_by_id('su').click()
        sleep(1)

    def test_q(self):
        print("tset_1")
        assert 3 == 1

    def test_w(self):
        print("tset_1")
        assert 1 == 1

    def test_e(self):
        print("tset_1")
        assert 1 == 1


    # def test_b(self):
    #     driver = self.driver
    #     driver.get('http://baidu.com')
    #     driver.find_element_by_id('kw').send_keys('蒙古')
    #     driver.find_element_by_id('su').click()
    #     sleep(2)


# suite = unittest.TestSuite()
# suite.addTest(test_unitt('test_a')) # 添加单个用例
# suite.addTests([TestUserLogin('test_user_reg_normal'),TestUserLogin('Test_User_login_password_wrong')]) # 添加多个用例
# unittest.TextTestRunner(verbosity=2).run(suite)
if __name__ == '__main__':
    unittest.main()