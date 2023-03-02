import openpyxl

class ReadExecl(object):
    

    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def open(self):
        self.wb = openpyxl.load_workbook(self.filename, data_only=True)
        self.sh = self.wb[self.sheetname]

    def read_data(self, start_number):
        self.open()
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
        self.open()
        datas = list(self.sh.rows)
        vars = {}
        # 读取变量数据到字典中
        for row in datas[start_number-1:]:
            var_names = row[name_column_number-1].value
            var_value = row[value_column_number-1].value
            vars[var_names] = var_value
        return vars



    def write_data(self,row,column,value):
        self.open()
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.filename)