import jsonpath
import requests
import json

'''
获取魔镜token
    验证码获取
    ↓
    验证码图像识别
    ↓
    token获取
'''
def get_token():
    # 获取验证码图像识别后的结果, 预期为4个字符
    url = "http://localhost:8081/"
    captcha = ""
    while len(captcha) != 4:
        response = requests.request("GET", url, data={})
        captcha = response.text

    url = "http://gateway.mj.cn/monitor/terminal/login"
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "username": "test123",
        "password": "axz+tev5OXSGM+sNATCulSx6N1t5Z9qDD33PGaq01ZBop745IVCcP5+t9Ua1bCMC",
        "uuid": "6cb13e75-971f-4cd6-8fa4-752e8074e4cc",
        "captcha": captcha
    })
    response = requests.post(url=url, data=payload, headers=headers)
    data = response.json()
    token = jsonpath.jsonpath(data, "$..token")
    #token = ["--------------------> token"]
    return(token[0])