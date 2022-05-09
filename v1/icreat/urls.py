from django.urls import path
from v1.icreat.views import SubjectCreateView, SubjectUpdateView, SubjectDeleteView, SubjectListView, SubjectRetrieveView


urlpatterns = [
path('/create',SubjectCreateView.as_view()),
path('/retrieve<int:pk>',SubjectRetrieveView.as_view()),
path('/update<int:pk>',SubjectUpdateView.as_view()),
path('/delete<int:pk>',SubjectDeleteView.as_view()),
path('/list',SubjectListView.as_view())
]