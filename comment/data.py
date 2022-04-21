import xlrd
import comment.logger

log = comment.logger.Logger()

class data():

    # 读取数据
    def read_data(self):
        personbook = xlrd.open_workbook("平城区网格员基本信息.xls")  # 打开指定文档
        sheetName = personbook.sheet_names()  # 获取表格所有sheet名称
        personlist = []

        for i in range(len(sheetName)): # 循环所有sheet
            personsheet = personbook.sheet_by_name(sheetName[i])  # 获取总表
            rows_old = personsheet.nrows  # 获取表格中已存在的数据的行数

            for j in range(1, rows_old): # 从第二行开始 ，循环所有行数
                person_phone = personsheet.cell_value(j, 2)  # 获取第三列 数据
                personlist.append(person_phone) # 追加手机号
        print(personlist)

        return personlist

