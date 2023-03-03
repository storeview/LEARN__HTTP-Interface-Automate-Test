import jsonpath
import requests
import json

'''
获取IPC Web 的登录token
'''
def get_token_of_ipc_web(url, username, password):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "action": "login",
        "username": username,
        "pwd": password,
    })
    response = requests.post(url=url, data=payload, headers=headers)
    data = response.json()
    token = jsonpath.jsonpath(data, "$..token")
    #token = ["--------------------> token"]
    return(token[0])