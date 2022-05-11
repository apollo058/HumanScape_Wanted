from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework import (mixins, generics)

from v1.icreat.serializers import IcreatSerializers
from v1.icreat.models import Icreat

class IcreatCreateView(CreateAPIView):
    """
    작성자 하정현:

    데이터 생성 View
    (POST)  /api/v1/icreat/create
    """
    serializer_class = IcreatSerializers

class IcreatUpdateView(generics.GenericAPIView,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin):
    """
    작성자: 하정현

    데이터 수정/삭제/특정uuid불러오기
    (GET)       /api/vi/icreat/create/<str:subject_num>
    (PATCH)     /api/vi/icreat/create/<str:subject_num>
    (DELETE)    /api/vi/icreat/create/<str:subject_num>
    """

    serializer_class = IcreatSerializers
    queryset = Icreat.objects.all()
    lookup_field = 'sub_num'

    def patch(self, request, sub_num: str):
        return self.update(request, sub_num, partial=True)
    
    def delete(self, request, sub_num: str):
        return self.destroy(request, sub_num)

    def get(self, request, sub_num: str):
        return self.retrieve(request, sub_num)