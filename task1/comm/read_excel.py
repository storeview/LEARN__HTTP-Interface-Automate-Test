import openpyxl
import re

class ReadExecl(object):
    

    def __init__(self, filename):
        self.filename = filename
        m = re.search(r'^(.*)\\([^\\]+).xlsx$',filename)
        file_parent_dir = m.group(1)
        name = m.group(2)
        self.new_filename = file_parent_dir + "\\"+"(测试结果记录)--" + name +".xlsx"

    def open(self, sheetname, data_only_flag):
        self.wb = openpyxl.load_workbook(self.filename, data_only=data_only_flag)
        self.sh = self.wb[sheetname]
        return self

    def sheet(self, sheetname):
        return self
    
    def close(self):
        self.wb.save(self.new_filename)

    def read_data(self, start_number):
        datas = list(self.sh.rows)
        title = [i.value for i in datas[0]]

        cases = []
        #存储测试用例的结构
        #[{a:a1, b:b1, c:c1}, {d:d1, e:e1, f:f1}]
        for i in datas[start_number-1:]:
            values = [c.value for c in i]
            case = dict(zip(title, values))
            cases.append(case)

        return cases

    def read_variable_data(self, start_number, name_column_number, value_column_number):
        datas = list(self.sh.rows)
        vars = {}
        # 读取变量数据到字典中
        for row in datas[start_number-1:]:
            var_names = row[name_column_number-1].value
            var_value = row[value_column_number-1].value
            vars[var_names] = var_value
        return vars



    def write_data(self,row,column,value):
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.new_filename)