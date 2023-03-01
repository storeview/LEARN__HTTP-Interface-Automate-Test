import unittest


"""一个测试用例模块"""
class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertTrue(1 == 2)

if __name__=='__main__':
    unittest.main()