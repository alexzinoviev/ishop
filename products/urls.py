from django.conf.urls import url
from .views import index, details, edit

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^details/(?P<slug>\S+)$', details, name='details'),
    url(r'^edit/(?P<slug>\S+)$', edit, name='edit'),
]
