from django.conf.urls import url
from shelf.views import FilmListView, FilmDetailView

urlpatterns = [
    url(r'^filmy/$', FilmListView.as_view(), name = 'film-list'),
    url(r'^filmy/(?P<pk>\d+)/$', FilmDetailView.as_view(), name = 'film-detail'),

]
