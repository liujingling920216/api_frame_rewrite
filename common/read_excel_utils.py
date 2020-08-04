import xlrd
from common.config_utils import config


class Read_Excel_Data:
    def __init__(self,sheet_name):
        self.excel_path = config.excel_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        wb = xlrd.open_workbook(self.excel_path)
        self.ws = wb.sheet_by_name(self.sheet_name)
        return self.ws

    def __get_merge_cell_list(self):
        self.merge_cell_list = self.sheet.merged_cells
        return self.merge_cell_list


    def __get_cell_value(self,row_index,col_index):
        for  (min_row,max_row,min_col,max_col) in self.__get_merge_cell_list():
            if row_index >= min_row and row_index < max_row:
                if col_index >= min_col and col_index < max_col:
                    value = self.ws.cell_value(min_row,min_col)
                    break   #匹配条件就退出，不然后面循环会把前面的值覆盖
                else:
                    value = self.ws.cell_value(row_index,col_index)
            else:
                value = self.ws.cell_value(row_index, col_index)
        return value

    def get_excel_case_data_by_dic(self):
        all_cases = []
        for r in range(1,self.sheet.nrows):
            case_data = {}
            for c in range(self.sheet.ncols):
                # 获取测试用例标题
                tiltle = self.__get_cell_value(0,c)
                data_value = self.__get_cell_value(r,c)
                # 构建测试用例字段标题(k),字段值(v)字典形式
                case_data[tiltle]=data_value
            all_cases.append(case_data)
        return  all_cases

if __name__ == "__main__":
    print(Read_Excel_Data('Sheet1').get_excel_case_data_by_dic())




