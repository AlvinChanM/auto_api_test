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
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)


    # 根据对应的case_id获得对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_value = self.get_row_value(row_num)
        return row_value


    # 根据对应的case_id找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        col_data = self.get_col_data()
        for coldata in col_data:
            if case_id in coldata:
                return num
            num += 1

    # 根据行号，找到对应的内容
    def get_row_value(self, row):
        return self.data.row_values(row)

    # 获取某一列的内容
    def get_col_data(self, col=None):
        if col != None:
            cols = self.data.col_values(col)
        else:
            cols = self.data.col_values(0)
        return cols

if __name__ == '__main__':
    oe = OperatingExcel()
    print oe.get_lines()