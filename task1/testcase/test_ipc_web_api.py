import unittest
from comm.get_token_of_ipc_web import get_token_of_ipc_web
from comm.read_excel import ReadExecl
from comm.handle_path import TESTCASE_FILE_PATH
from ddt import ddt, data
import requests
import json
from comm.assert_two_json_equal import assert_two_json_equal
from comm.replace_variable import replace_variable
from comm.write_log import log

"""
测试魔镜接口
1. 获取登录token
    - 在整个测试过程中, 只需要获取一次.
2. 准备测试数据
    - 从Excel数据源中导入数据
3. 执行请求
    - 解析请求的数据, 并进行发送
4. 响应断言
    - 对返回值进行断言
5. 测试报告输出
"""
@ddt
class IPCWebTestCase(unittest.TestCase):
    
    excel =  ReadExecl(TESTCASE_FILE_PATH)
    #测试用例数据
    testcase_data = excel.open("IPCWeb测试用例", True).read_data(3)
    #变量列表数据
    variables = excel.open("变量列表", True).read_variable_data(3, 7, 8)

    sheet =  excel.open("IPCWeb测试用例", True)


    @classmethod
    def setUpClass(cls):
        #获取魔镜token, 只执行一次
        first_testcase = IPCWebTestCase.testcase_data[0]
        ret = replace_variable(first_testcase, IPCWebTestCase.variables)
        IPCWebTestCase.token = get_token_of_ipc_web(ret["url"], IPCWebTestCase.variables["EncryptedUsername"], IPCWebTestCase.variables["EncryptedPassword"])
        log.info("获取魔镜token: {}".format(IPCWebTestCase.token))

    @data(*testcase_data[1:])
    def test_api(self, value):
        #准备数据
        # 变量替换(将字符串中用{{}}圈起来的变量, 替换成本来的值)
        self.variables["token"] = IPCWebTestCase.token
        ret=replace_variable(value, self.variables)
        method = ret["method"]
        url = ret["url"]
        module = ret["module"]
        headers = ret["headers"]
        payload = ret["payload"]
        resp = None
        no = ret["no"]
        title = ret["title"]
        
        #执行请求
        log.info("执行用例编号: {}".format(no))
        if method == "GET":
            payload = json.loads(payload)
            resp = requests.get(url, params=payload, headers=headers)
        elif method == "POST":
            resp = requests.post(url, data=payload, headers=headers)
        
        #打印请求过程
        print("\n用例编号: {}\n测试内容: [{}] {}\n{}请求地址: {}\n请求头: {}\n请求体: \n{}".format(no, module, title, method, url, headers, payload))
        print("原始响应(raw): \n{}\n".format(resp.text))
        print("响应内容(json): \n{}".format(resp.json()))

        #记录返回值到Excel中
        row_number = ret["row_number"]
        col_number = ret["col_number"]
        IPCWebTestCase.sheet.write_data(row_number, col_number, json.dumps(resp.json()))

        #响应断言
        try:
            #1.返回码为200(成功)
            self.assertEqual(resp.status_code, 200)
            #2.断言两个json值完全一致
            expect_json = json.loads(ret["assert"])
            #打印预期相应
            print("预期响应: \n{}\n\n".format(expect_json))
            
            self.assertTrue(assert_two_json_equal(expect_json, resp.json(), "$"), "和预期的JSON值不同") 
            IPCWebTestCase.sheet.write_data(row_number, col_number+1, "Pass")
            log.warning("用例断言成功!")
        except AssertionError as e:
            #如果try中有两个断言, 这里AssertionError只根据第一个断言的结果进行判断.
            log.warning("用例断言失败!")
            IPCWebTestCase.sheet.write_data(row_number, col_number+1, "Fail")
            raise e


    @classmethod
    def tearDownClass(cls):
        IPCWebTestCase.excel.close()

if __name__=='__main__':
    unittest.main()