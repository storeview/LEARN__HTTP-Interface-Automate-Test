import unittest

"""
setUpClass
tearDownClass
两个分别在测试**类**执行前后运行, 代表只执行一次时的, 前置条件和清理动作.
"""
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("对于类的最开始, 需要有的前置操作.")
    
    def test_1(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_2(self):
        self.assertEqual('foo'.upper(), 'f00')

    def test_3(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @classmethod
    def tearDownClass(cls):
        print("对于类的最后, 需要执行的清理工作.")

if __name__ == '__main__':
    unittest.main()