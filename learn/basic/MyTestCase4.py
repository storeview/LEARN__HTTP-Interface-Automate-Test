import unittest

"""

"""

#@unittest.skip("也可以跳过类")
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("对于类的最开始, 需要有的前置操作.")
    
    def test_1(self):
        print(1)
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skip("将 unittest 作用在方法名上, 可以跳过测试方法")
    def test_2(self):
        print(2)
        self.assertEqual('foo'.upper(), 'f00')

    def test_3(self):
        print(3)
        self.skipTest("可以直接在方法中跳过")
        self.assertEqual('foo'.upper(), 'FOO')

    @classmethod
    def tearDownClass(cls):
        print("对于类的最后, 需要执行的清理工作.")

if __name__ == '__main__':
    unittest.main()