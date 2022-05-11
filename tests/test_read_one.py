from rest_framework.test import APITestCase
from rest_framework import status

class TestIcreatReadOne(APITestCase):

    UPLOAD_API = '/api/v1/icreat/create'
    API = '/api/v1/icreat'

    req = {
            "subject"       : '조직구증식증 임상연구 네트워크 구축 및 운영(HLH)',
            "sub_num"       : 'C130010',
            "period"        : '3년',
            "boundary"      : '국내다기관',
            "remark"        : '관찰연구',
            "institute"     : '서울아산병원',
            "trial"         : "코호트",
            "goal_research" : "120",
            "meddept"       : 'Pediatrics'
        }

    def setUp(self):
        # 업로드
        self.assertEqual(self.client.post(self.UPLOAD_API, data=self.req).status_code,
                        201)
    
    def test_read(self):
        req = self.req.copy()
        res = self.client.get(f"{self.API}/{req['sub_num']}")
        self.assertEqual(res.status_code, 200)

    def test_read_failed(self):
        # 없는 sub num
        res = self.client.get(f"{self.API}/CVDSDFS", data={'period': '10년'})
        self.assertEqual(res.status_code, 404)
