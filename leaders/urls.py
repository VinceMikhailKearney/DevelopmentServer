from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /leaders/mlas
    url(r'^mlas/$', views.fetchMlas, name='fetchMlas'),
]