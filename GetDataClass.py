import xlrd
import logger

log = logger.Logger()

class data():

    # 读取网格长数据
    def read_wgz(self):
        wgz_book = xlrd.open_workbook("平城区网格长基本信息.xls")  # 打开指定文档
        sheetName = wgz_book.sheet_names()  # 获取表格所有sheet名称
        wgz_list = []

        for i in range(len(sheetName)): # 循环所有sheet
            wgz_sheet = wgz_book.sheet_by_name(sheetName[i])  # 获取总表
            rows_old = wgz_sheet.nrows  # 获取表格中已存在的数据的行数

            for j in range(1, rows_old): # 从第二行开始 ，循环所有行数
                wgz_phone = wgz_sheet.cell_value(j, 2)  # 获取第三列 数据
                if wgz_phone == '':
                    continue
                wgz_list.append(wgz_phone) # 追加手机号
        # print(wgz_list)
        # print(len(wgz_list))

        return wgz_list


    # 读取运行结果文件，获取已提交事件的网格员
    def read_test(self):
        wgy_book = xlrd.open_workbook("上传事件运行结果.xlsx")  # 打开指定文档
        sheetName = wgy_book.sheet_names()  # 获取表格所有sheet名称
        wgy_list = []

        for i in range(len(sheetName)): # 循环所有sheet
            wgy_sheet = wgy_book.sheet_by_name(sheetName[i])  # 获取总表
            rows_old = wgy_sheet.nrows  # 获取表格中已存在的数据的行数

            for j in range(1, rows_old): # 从第二行开始 ，循环所有行数
                wgy_phone = wgy_sheet.cell_value(j, 6)  # 获取第三列 数据
                if wgy_phone not in wgy_list:
                    wgy_list.append(wgy_phone) # 追加手机号
        print(wgy_list)

        return wgy_list

if __name__ == '__main__':
    data().read_wgz()