from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'', views.ListSongsView.as_view(), name="songs-all")
]
