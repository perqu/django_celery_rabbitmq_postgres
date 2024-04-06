from django.contrib import admin
from django.urls import path
from core.views import health_check, view1, view2, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('button1/', view1, name='view1'),
    path('button2', view2, name='view2'),
    path('health/', health_check, name='health_check'),
]
