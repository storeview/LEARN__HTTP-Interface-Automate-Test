import unittest
import json


#得到对象的类型
def get_type_by_object(obj):
    return type(obj)

#是否为空对象(即{})
def is_empty_object(expect_json):
    for key in expect_json:
        return False
    return True

#递归判断两个json值
def assert_two_json_equal(expect_json, new_json, jsonpath):
    if (expect_json == None or is_empty_object(expect_json)):
        return
    for k in expect_json:
        cur_jsonpath = jsonpath + "." + str(k)
        if get_type_by_object(expect_json[k]) == list or get_type_by_object(expect_json[k]) == dict:
            try:
                new_json = new_json[k]
            except:
                new_json = None
            if get_type_by_object(expect_json) == list:
                assert_two_json_equal(expect_json[k], new_json, jsonpath+"["+str(k)+"]")
            else:
                assert_two_json_equal(expect_json[k], new_json, cur_jsonpath)
        else:
            test_name = "{}值为{}".format(cur_jsonpath, expect_json[k])
            print(test_name)
            if new_json != None:
                print()
            else:
                print()
            #unittest.TestCase.assertEqual(new_json[k], expect_json[k])


if __name__=="__main__":
    json1 = json.loads('{"code":200,"message":"success","data":{"lightAlarmType":2,"audioAlarmFiles":[{"name":"警报音","index":1,"type":1,"status":0},{"name":"请注意，您已进入监控区域","index":2,"type":1,"status":0},{"name":"危险区域，请勿靠近","index":3,"type":1,"status":1},{"name":"您好，欢迎光临","index":4,"type":1,"status":0}],"audioAlarmStatus":2,"lightAlarmStatus":2,"audioPlayCount":1,"lightAlarmFrequency":2,"lightAlarmTime":5,"gbAlarmStatus":1}}')
    json2 = json.loads('{"code": 401, "message": "未授权"}')
    assert_two_json_equal(json1, json2, "$")