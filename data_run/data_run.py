import unittest
import paramunittest
from common.request_utils import RequestsUtils
from common.case_data_utils import CaseData

casedata = CaseData().get_test_data_by_list()
@paramunittest.parametrized(
    *casedata
)
class RunData(paramunittest.ParametrizedTestCase):
    def setParameters(self, case_id,case_info ):
        self.case_id = case_id
        self.case_info = case_info

    def test_case(self):
            RequestsUtils().case_step(self.case_info)

if __name__ == '__main__':
    unittest.main()