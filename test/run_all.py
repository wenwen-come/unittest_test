import unittest
import sys
sys.path.append(r'./')
import HTMLTestRunnerCN
# from HTMLTestRunnerCN import  HTMLTestRunner
import HTMLTestRunnerCN

suite = unittest.defaultTestLoader.discover("./")

f = open("report.html", 'wb') # 二进制写格式打开要生成的报告文件
#HTMLTestRunnerCN.HTMLTestReportCN(stream=f,title="Api Test",description="测试描述",tester="卡卡").run(suite)

res = HTMLTestRunnerCN.HTMLTestReportCN(stream=f,title="Api Test",description="测试描述",tester="wenyy")
res.run(suite)

f.close()
#



# if __name__ == '__main__':
#     filePath ='F:\\Report.html'
#     # fp = file(filePath,'wb')
#     f = open("report.html", 'wb')
#     runner = HTMLTestRunnerCN.HTMLTestRunner(
#         stream=f,
#         title='{ Test Report }',
#         #description='',
#         #tester="Findyou"
#         )
#     runner.run()