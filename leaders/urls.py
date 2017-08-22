from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /leaders/mlas
    url(r'^$', views.local_ping, name="local_ping"),
    url(r'^mlas/$', views.fetchMlas, name='fetchMlas'),
    url(r'^parties/$', views.fetchParties, name='fetchParties'),
    url(r'^plainMlaData/$', views.plainMlaData, name='plainMlaData'),
]