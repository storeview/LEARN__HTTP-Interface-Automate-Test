import os


"""
处理文件/文件夹路径的拼接, 并以大写的方式作为参数传递
"""

#项目文件夹当前路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#用例模块路径
TESTCASE_DIR = os.path.join(BASE_DIR, "testcase")
#数据模块路径
DATA_DIR = os.path.join(BASE_DIR, "datasource")
#测试报告路径
REPORT_DIR = os.path.join(BASE_DIR, "report")
#日志文件路径
LOG_DIR = os.path.join(BASE_DIR, "logs")


#测试用例Excel表格路径
TESTCASE_FILE_PATH = os.path.join(DATA_DIR, "自动化测试-数据源.xlsx")
#测试报告HTML路径
REPORT_FILE_PATH = os.path.join(REPORT_DIR, "report.html")