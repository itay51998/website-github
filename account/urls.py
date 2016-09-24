from django.conf.urls import url
from . import views
from django.conf import settings

app_name = 'account'

urlpatterns = [
    url(r'^$', views.index, name='index', {'document_root': settings.STATIC_ROOT}),
]