import unittest
import json


#得到对象的类型
def typeof(obj):
    return type(obj)

#是否为空对象(即{})
def is_empty_object(expect_json):
    for key in expect_json:
        return False
    return True


#递归判断两个json值
def assert_two_json_equal(expect_json, new_json, jsonpath):
    #无递归终止条件
    ret = True

    #当前对象是列表
    if typeof(expect_json) == list:
        for index, item in enumerate(expect_json):
            try:
                new_json2=new_json[index]
            except:
                new_json2=None
            ret = ret and assert_two_json_equal(expect_json[index], new_json2, jsonpath+"["+str(index)+"]")
    #当前对象是字典
    elif typeof(expect_json) == dict:
        for index, item in enumerate(expect_json):
            try:
                new_json2=new_json[item]
            except:
                new_json2=None
            ret = ret and assert_two_json_equal(expect_json[item], new_json2, jsonpath+"."+item)
    #当前对象是字符串, 数字, 布尔值, 空值
    else:
        test_name = "{} 值为 {}".format(jsonpath, expect_json)
        if expect_json == new_json:
            print("{} - {}".format(True, test_name))
        else:
            print("--------------------> {} - {} <--------------------".format(False, test_name))
        #断言结果
        if expect_json != new_json:
            return False
        return True
    return ret

if __name__=="__main__":
    json1 = json.loads('{"code":200,"message":"success","data":{"smartStatus":1,"defenceStatus":1,"defenceTime":null,"eventStatus":1,"action":[1],"sensitivity":70,"screenShotStatus":2,"smartType":[1],"areaGroup":[{"resolution":"1920*1080","points":["0,0","0,1080","1920,1080","1920,0"]}],"showArea":2}}')
    json2 = json.loads('{"code": 401, "message": "未授权"}')
    assert_two_json_equal(json1, json2, "$")


