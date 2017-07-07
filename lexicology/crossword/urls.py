from django.conf.urls import url
from crossword.views import index

urlpatterns = [
    url(r'^$', index.IndexView.as_view(), name='index'),
]