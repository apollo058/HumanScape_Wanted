from rest_framework.test import APITestCase
from rest_framework import status

class TestIcreatCreate(APITestCase):
    """
    작성자: 하정현

    필수 구현사항이 아닌 데다, 마감 문제로
    간단한 테스트 코드 구현만 함
    """
    API = '/api/v1/icreat/create'
    
    def test_create(self):
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

        self.assertEqual(self.client.post(self.API, data=req).status_code,
                        201)

    def test_upload_same_failed(self):
        
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

        self.assertEqual(self.client.post(self.API, data=req).status_code,
                        201)
        self.assertEqual(self.client.post(self.API, data=req).status_code,
                        400)