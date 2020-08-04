from common.read_excel_utils import Read_Excel_Data

class CaseData:
    def __init__(self,sheet_name='Sheet1'):
        self.excel_data = Read_Excel_Data(sheet_name).get_excel_case_data_by_dic()


    def __get_test_data_by_dic(self):
        "这个方法主要是处理读取excel多个步骤，合并成一行"
        case_dict = {}
        for i in self.excel_data:
            case_dict.setdefault(i['测试用例编号'], []).append(i)
        return case_dict

    def get_test_data_by_list(self):
        case_list = []
        for k, v in self.__get_test_data_by_dic().items():
            case_dict1 = {}
            case_dict1["case_id"] = k
            case_dict1["case_info"] = v
            case_list.append(case_dict1)
        return case_list


if __name__ == '__main__':
    casedata = CaseData().get_test_data_by_list()
    for i in casedata:
        print(i)

