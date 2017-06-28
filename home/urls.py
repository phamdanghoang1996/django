from django.conf.urls import url
from . import views #Doan nay import cai view co ne!

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
