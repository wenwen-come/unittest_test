import unittest
import requests
import json

class TestUserLogin(unittest.TestCase):
    url_login = "http://10.1.1.171:8080/api/account/user-login/login"

    # 登录成功
    def test_user_login_normal(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.6 Safari/537.36',
            'Content-Type': 'application/json'
        }
        data = {"account":"wenyy",
                "password":"e10adc3949ba59abbe56e057f20f883e"}
        respone = requests.post(url=self.url_login, headers=headers, data=json.dumps(data))
        # print(respone.text)
        res = respone.json()["message"]
        self.assertIn('操作成功！',res)

    def Test_User_login_password_wrong(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.6 Safari/537.36',
            'Content-Type': 'application/json'
        }
        data = {"account": "wenyy",
                "password": "e10adc3949ba59abbe56e057f20f111e"}
        respone = requests.post(url=self.url_login, headers=headers, data=json.dumps(data))
        # print(respone.text)
        res = respone.json()["message"]
        self.assertIn('账号或密码错误！', res)




# suite = unittest.TestSuite()
# suite.addTest(TestUserLogin('test_user_login_normal')) # 添加单个用例
# suite.addTests([TestUserLogin('test_user_reg_normal'),TestUserLogin('Test_User_login_password_wrong')]) # 添加多个用例
# unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    unittest.main(verbosity=2)
