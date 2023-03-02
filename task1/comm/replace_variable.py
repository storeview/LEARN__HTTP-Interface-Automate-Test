import re


def replace_variable(value, variables):
        url = variables["server_url"]+value["url"]
        method = value["method"]
        payload = value["payload"]
        #替换变量
        payload = replace0(payload, variables)
        url = replace0(url, variables)
        method = replace0(method, variables)
        headers = {}

        if value["headers"] != None:
            #替换变量
            headers_str = replace0(value["headers"], variables)
            headers_str = headers_str.split(";")
            header_names = [h.split(':')[0] for h in headers_str]
            header_vals = [h.split(':')[1] for h in headers_str]
            headers = dict(zip(header_names, header_vals))
        return {"url":url, "method":method, "payload":payload, "headers":headers}

def replace0(str, variables):
    #寻找变量
    result = re.search(r"{{([a-zA-Z0-9]+)}}", str)
    while result != None:
        #替换变量
        str = str.replace('{{'+result.group(1)+'}}', variables[result.group(1)])
        result = re.search(r"{{([a-zA-Z0-9]+)}}", str)
    return str


