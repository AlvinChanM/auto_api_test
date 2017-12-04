# coding=utf-8
import xlrd
class OperatingExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = r"C:\Users\Administrator\Desktop\workspace\auto_api_test\case_data\interface.xlsx"
            self.sheet_id = 0
        self.data = self.get_data()
    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

if __name__ == '__main__':
    oe = OperatingExcel()
    print oe.get_lines()