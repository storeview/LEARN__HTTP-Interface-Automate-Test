from openpyxl import Workbook

import jsonpath
import json


#obj = json.loads('{"data":{"audio_enable":1,"audio_input_enable":1,"audio_input_format":{"select_content":[{"id":0,"name":"G711U"},{"id":1,"name":"G711A"}],"select_index":1},"in_volume":{"current":11,"range":[0,100]},"out_volume":{"current":11,"range":[0,100]},"silence_upgrade_enable":1},"err_code":0,"err_msg":"ok","req_id":"50796871-4B58-6E46-97E3-72C5BD5D9E4B"}')
obj = json.loads('{"data": 123, "data2":23}')
print(type(obj))
print(obj)
ret = jsonpath.jsonpath(obj, '$.data')


print(ret)