from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from uritemplate import partial
from .serializers import IcreatSerializer
from .models import Icreat
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from v1.icreat.models import Icreat

'''
작성자 : 남기윤, 하정현
'''

class SubjectDetailView(RetrieveUpdateDestroyAPIView):
    model = Icreat
    serializer_class = IcreatSerializer
    
    def get_queryset(self):
        res = Icreat.objects.all()
        return res

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def patch(self, request, pk):
        return self.update(request, pk, partial = True)
    
    def delete(self, request, pk):
        """
        is_active가 False로 처리되어야 한다.
        """
        obj = get_object_or_404(Icreat, id=pk)
        if not obj.is_active:
            # 이미 삭제처리됨
            return Response({"error": "already deleted"}, status=status.HTTP_400_BAD_REQUEST)
        obj.is_active = False
        obj.save()
        return Response({"is_active": obj.is_active}, status=status.HTTP_204_NO_CONTENT)

class SubjectListView(ListCreateAPIView): #/api/v1/icreat/list
    model = Icreat
    serializer_class = IcreatSerializer

    def get_queryset(self):
        page = self.request.GET.get('page',1)
        pagesize = 10
        limit = pagesize * page
        offset = limit -pagesize
        a_week_ago = datetime.today() - timedelta(days = 7)
        subjects = Icreat.objects.filter(modified_at__gte=a_week_ago)[offset:limit]
        return subjects
