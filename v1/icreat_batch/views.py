import time

from datetime import datetime

from django.db.utils import IntegrityError

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..icreat.models import Icreat
from .utils import get_data

class IcreatBatchView(APIView):
    def post(self, request):
        create_data = 0
        update_data = 0
        start_time = time.time()
        batch_data = get_data()
        for data in batch_data['data']:
            set_col_name_data = {
            "subject"       : data["과제명"],
            "sub_num"       : data["과제번호"],
            "period"        : data["연구기간"],
            "boundary"      : data["연구범위"],
            "remark"        : data["연구종류"],
            "institute"     : data["연구책임기관"],
            "trial"         : data["임상시험단계(연구모형)"],
            "goal_research" : data["전체목표연구대상자수"],
            "meddept"       : data["진료과"]
            }
            try:
                Icreat.objects.create(**set_col_name_data)
                create_data += 1
            except IntegrityError:
                exist_data = (Icreat.objects
                .filter(sub_num=data["과제번호"])
                .values('subject', 'sub_num', 'period', 'boundary', 'remark', 'institute', 'trial', 'goal_research', 'meddept'))
                if exist_data[0] == set_col_name_data:
                    continue
                else:
                    exist_data.update(**set_col_name_data, modified_at = datetime.now())
                    update_data += 1
        end_time = time.time()
        print("WorkingTime: {} sec".format(end_time-start_time))
        print({"create_data" : create_data, "update_data" : update_data})
        return Response({'message' : "success!"}, status=status.HTTP_201_CREATED)
