from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="post_index"),
    # localhost:8000/blog
    url(r'^post/(?P<post_id>\d+)/$', views.detail, name="post_detail"),
    # localhost:8000/blog/post/123/
    url(r'^post/new/$', views.post_new, name="post_new"),
    # localhost:8000/blog/post/new
    url(r'^post/(?P<post_id>\d+)/edit/$', views.post_edit, name="post_edit"),
]

