from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /leaders/mlas
    url(r'^mlas/$', views.fetchMlas, name='fetchMlas'),
    url(r'^niamh/$', views.niamh, name='niamh'),
]