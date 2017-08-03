from django.conf.urls import url
from .views import index, details, edit
from django.views.generic.list import ListView
from .models import Product

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list$', ListView.as_view(
        model=Product,
        paginate_by=2,
        template_name='list.html'
    )
        ),
    url(r'^details/(?P<slug>\S+)$', details, name='details'),
    url(r'^edit/(?P<slug>\S+)$', edit, name='edit'),
]
