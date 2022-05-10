from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import IcreatSerializer
from .models import Icreat
from datetime import datetime, timedelta

'''
작성자 : 남기윤
'''



class SubjectDetailView(RetrieveUpdateDestroyAPIView):
    model = Icreat
    serializer_class = IcreatSerializer
    
    def get_queryset(self):
        res = Icreat.objects.all()
        return res

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

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