import unittest
from comm.handle_path import TESTCASEDIR


"""
执行测试主程序
"""

#新建测试套件.
suite = unittest.TestSuite()
#新建加载器. 用于从指定目录, 类, 模块下加载测试用例
loader = unittest.TestLoader()
#套件中添加测试, 并从指定测试用例目录下加载测试用例集群
suite.addTest(loader.discover(TESTCASEDIR))
#测试执行
runner = unittest.TextTestRunner()

#执行测试套件
runner.run(suite)