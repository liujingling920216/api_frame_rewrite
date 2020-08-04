import os
import xlrd

excel_path = '..\data\\test_case.xlsx'
data_path = os.path.join(os.path.dirname(__file__),excel_path)

wb = xlrd.open_workbook(data_path)
ws = wb.sheet_by_name('Sheet1')

# excel中没有合并单元格实现方式
# all_cases = {}
# for r in range(1,ws.nrows):
#     case_data = {}
#     for c in range(ws.ncols):
#         # 获取测试用例标题
#         tiltle = ws.cell_value(0,c)
#         data_value = ws.cell_value(r,c)
#         # 构建测试用例字段标题(k),字段值(v)字典形式
#         case_data[ws.cell_value(0,c)]=data_value
#     # 构建测试用例名(k),用例信息(v)字典形式
#     all_cases[ws.cell_value(r,0)]=case_data
# print(all_cases)

# 获取有合并单元格的实现方式
merge_cell_list = ws.merged_cells   #（起始行索引，结束行索引，起始列索引，结束列索引）
row_index = 11
col_index = 2

def get_cell_value(row_index,col_index):
    for  (min_row,max_row,min_col,max_col) in merge_cell_list:
        if row_index >= min_row and row_index < max_row:
            if col_index >= min_col and col_index < max_col:
                value = ws.cell_value(min_row,min_col)
                break   #匹配条件就退出，不然后面循环会把前面的值覆盖
            else:
                value = ws.cell_value(row_index,col_index)
        else:
            value = ws.cell_value(row_index, col_index)
    return value

def get_excel_case_data_by_dic():
    all_cases = []
    for r in range(1,ws.nrows):
        case_data = {}
        for c in range(ws.ncols):
            # 获取测试用例标题
            tiltle = get_cell_value(0,c)
            data_value = get_cell_value(r,c)
            # 构建测试用例字段标题(k),字段值(v)字典形式
            case_data[tiltle]=data_value
        # # 构建测试用例名(k),用例信息(v)字典形式
        # all_cases[get_cell_value(r,0)]=case_data
        all_cases.append(case_data)
    return  all_cases

for i in get_excel_case_data_by_dic():
    print(i)


get_excel_case_data_by_dic()










