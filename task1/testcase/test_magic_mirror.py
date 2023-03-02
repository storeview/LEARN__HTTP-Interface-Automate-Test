import unittest
from comm.get_token import get_token
from comm.read_excel import ReadExecl
from comm.handle_path import TESTCASE_FILE_PATH
from ddt import ddt, data
import requests
import json
from comm.assert_two_json_equal import assert_two_json_equal
from comm.replace_variable import replace_variable

"""
测试魔镜接口

1. 获取token(依赖于验证码识别服务, 即调用其他程序)
    - 在整个测试过程中, 只需要获取一次.
    - 通过http接口获取验证码识别结果
2. 准备测试数据
    - 从Excel数据源中导入数据
3. 执行请求
    - 解析请求的数据, 并进行发送
4. 响应断言
    - 对返回值进行断言
5. 测试报告输出
"""
@ddt
class MagicMirrorTestCase(unittest.TestCase):
    
    #测试用例数据
    testcase_data = ReadExecl(TESTCASE_FILE_PATH, "MagicMirror测试用例").read_data(3)
    #变量列表数据
    variables = ReadExecl(TESTCASE_FILE_PATH, "变量列表").read_variable_data(2, 1, 2)

    @classmethod
    def setUpClass(cls):
        #获取魔镜token, 只执行一次
        MagicMirrorTestCase.token = get_token()
        print()
    
    @data(*testcase_data)
    def test_api(self, value):
        #准备数据
        # 变量替换(将字符串中用{{}}圈起来的变量, 替换成本来的值)
        self.variables["token"] = MagicMirrorTestCase.token
        ret=replace_variable(value, self.variables)
        method = ret["method"]
        url = ret["url"]
        payload = ret["payload"]
        headers = ret["headers"]
        resp = None
        
        #执行请求
        if method == "GET":
            resp = requests.get(url, params=payload, headers=headers)
        elif method == "POST":
            resp = requests.get(url, data=payload, headers=headers)
        
        #打印请求过程
        no = value["no"]
        title = value["title"]
        print("\n用例编号: {}\n测试内容: {}\n{}请求地址: {}\n请求头: {}\n请求体: \n{}".format(no, title, method, url, headers, payload))

        #打印响应内容
        print("响应内容: \n{}".format(resp.json()))


        #响应断言
        #1.返回码为200(成功)
        self.assertEqual(resp.status_code, 200)
        #2.断言两个json值完全一致
        expect_json = json.loads(value["assert"])
        #打印预期相应
        print("预期相应: \n{}\n\n".format(expect_json))
        self.assertTrue(assert_two_json_equal(expect_json, resp.json(), "$")) 
        

if __name__=='__main__':
    unittest.main()