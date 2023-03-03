import re


def replace_variable(data, variables):
        for key in data:
            #替换变量
            if data[key] == None or type(data[key]) == int:
                 continue
            data[key] = replace0(data[key], variables)
            if key == "url":
                  data[key]=variables["server_url"]+data[key]
            elif key == "headers":
                headers_str = replace0(data["headers"], variables)
                headers_str = headers_str.split("$$$")
                header_names = [h.split(':')[0].strip() for h in headers_str]
                header_vals = [h.split(':')[1].strip() for h in headers_str]
                data[key] = dict(zip(header_names, header_vals))                
        return data

def replace0(str, variables):
    #寻找变量
    result = re.search(r"{{([a-zA-Z0-9]+)}}", str)
    while result != None:
        #替换变量
        str = str.replace('{{'+result.group(1)+'}}', variables[result.group(1)])
        result = re.search(r"{{([a-zA-Z0-9]+)}}", str)
    return str