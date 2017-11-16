from django.conf.urls import url
from shelf.views import (DirectorListView, DirectorDetailView, FilmListView, FilmDetailView)
from rent.views import FilmRentView

urlpatterns = [
    url(r'^directors/$', DirectorListView.as_view(), name = 'director-list'),
    url(r'^directors/(?P<pk>\d+)/$', DirectorDetailView.as_view(), name = 'director-detail'),
    url(r'^films/$', FilmListView.as_view(), name = 'film-list'),
    url(r'^films/(?P<pk>\d+)/$', FilmDetailView.as_view(), name = 'film-detail'),
    url(r'^films/(?P<pk>\d+)/rent/$', FilmRentView.as_view(), name = 'film-rent'),

]
