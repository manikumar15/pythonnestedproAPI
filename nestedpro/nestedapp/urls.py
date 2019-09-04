from django.conf.urls import url

from .views import AuthorListView,AuthorDetailView,BookListView,BookDetailView

urlpatterns = [
	url(r'^author-api/$',AuthorListView.as_view()),
	url(r'^author-api/(?P<pk>\d+)$',AuthorDetailView.as_view()),

	url(r'^book-api/$',BookListView.as_view()),
	url(r'^book-api/(?P<pk>\d+)$',BookDetailView.as_view()),

]