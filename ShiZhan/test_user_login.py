import unittest
import requests
import sys
sys.path.append(r'./')
import read_excel # 导入read_excel中的方法
import json  # 用来转化excel中的json字符串为字典

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list = read_excel.excel_to_list("test_user_data.xlsx", "TestUserLogin")  # 读取该测试类所有用例数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_user_login_normal(self):
        case_data = read_excel.get_test_data(self.data_list, '001')   # 从数据列表中查找到该用例数据
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('接口地址')   # 从字典中取数据，excel中的标题也必须是小写url
        data = case_data.get('请求参数')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('预期返回数据')  # 期望数据
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.6 Safari/537.36',
            'Content-Type': 'application/json'
        }

        res = requests.post(url=url, headers=headers,data=json.loads(data))  # 表单请求，数据转为字典格式
        # respone = res.json()
        self.assertEqual(res.text, expect_res)  # 改为assertEqual断言

if __name__ == '__main__':   # 非必要，用于测试我们的代码
    unittest.main()
