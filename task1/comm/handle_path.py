import os


"""
处理文件/文件夹路径的拼接, 并以大写的方式作为参数传递
"""

#项目文件夹当前路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#用例模块路径
TESTCASEDIR = os.path.join(BASEDIR, "testcase")