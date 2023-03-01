import unittest

"""
setup
tearDown
两个分别在测试方法执行前后运行, 代表前置条件和清理动作.
"""
class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("对于每一个测试, 都需要有的前置操作.")
    
    def test_1(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_2(self):
        self.assertEqual('foo'.upper(), 'f00')

    def test_3(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def tearDown(self):
        print("对于每一个测试, 都需要执行的清理工作.")

if __name__ == '__main__':
    unittest.main()