from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lazy_load_posts/$', views.lazy_load_posts, name='lazy_load_posts'),
]
