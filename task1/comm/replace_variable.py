import re


result = re.search(r"{{[a-zA-Z0-9]+}}", '{"deviceCode":"{{SN}}","token":"{{token}}"}')

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
            headers_str = value["headers"].split(';')
            #替换变量
            headers_str = replace0(headers_str, variables)
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