import unittest
from comm.handle_path import TESTCASE_DIR, REPORT_FILE_PATH
from report.HwTestReport_local import HTMLTestReport
from lib.HTMLTestRunnerNew import HTMLTestRunner

"""
执行测试主程序
"""

#新建测试套件.
suite = unittest.TestSuite()
#新建加载器. 用于从指定目录, 类, 模块下加载测试用例
loader = unittest.TestLoader()
#套件中添加测试, 并从指定测试用例目录下加载测试用例集群
suite.addTest(loader.discover(TESTCASE_DIR))


#unittest.TextTestRunner().run(suite)
#'''
with open(REPORT_FILE_PATH, 'wb') as report:
    runner = HTMLTestReport(stream=report,
                            title="自动化测试报告",
                            description="魔镜终端协议测试(参数获取及设置)",
                            tester='llf')
    #执行测试套件
    runner.run(suite)
#'''