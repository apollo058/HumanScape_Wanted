from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import IcreatSerializer, IcreatDeleteSerializer
from .models import Icreat
from datetime import datetime, timedelta

'''
작성자 : 남기윤
'''

class SubjectCreateView(CreateAPIView): #/api/v1/icreat/create
    model = Icreat
    serializer_class = IcreatSerializer

class SubjectRetrieveView(RetrieveAPIView): #/api/v1/icreat/retrieve
    model = Icreat
    serializer_class = IcreatSerializer

class SubjectUpdateView(UpdateAPIView): #/api/v1/icreat/update
    model = Icreat
    serializer_class = IcreatSerializer

    def get_success_url(self):
        return JsonResponse(self.queryset, status = 200) 

class SubjectDeleteView(UpdateAPIView): #/api/v1/icreat/delete
    model = Icreat
    serializer_class = IcreatDeleteSerializer

class SubjectListView(ListCreateAPIView): #/api/v1/icreat/list
    model = Icreat
    serializer_class = IcreatDeleteSerializer

    def get_queryset(self):
        page = self.request.GET.get('page',1)
        pagesize = 10
        limit = pagesize * page
        offset = limit -pagesize
        a_week_ago = datetime.today() - timedelta(days = 7)
        subjects = Icreat.objects.filter(modified_at__gte=a_week_ago)[offset:limit]
        return subjects