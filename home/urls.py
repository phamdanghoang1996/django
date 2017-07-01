from django.conf.urls import url
from . import views #Doan nay import cai view co ne!

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'congnghe', views.congnghe, name='congnghe'),
    url(r'khoahoc', views.khoahoc, name='khoahoc'),
    url(r'thethao', views.thethao, name='thethao'),
    url(r'phapluat', views.phapluat, name='phapluat'),
    url(r'game', views.game, name='game'),
]
