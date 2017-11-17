from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^users/', include('django.contrib.auth.urls')),
]


