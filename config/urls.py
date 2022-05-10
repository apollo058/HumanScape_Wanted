from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/icreat', include('v1.icreat.urls')),
    path('api/v1/batch', include('v1.icreat_batch.urls'))
]
