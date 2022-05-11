from django.urls import path
from v1.icreat.views import *

urlpatterns = [
    path('/create', IcreatCreateView.as_view()),
    path('/<str:sub_num>', IcreatUpdateView.as_view())
]