import unittest

"""
最简单的一个测试用例 test case
"""
class MyTestCase(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()