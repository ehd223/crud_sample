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
    url(r'^post/(?P<post_id>\d+)/delete/$', views.post_delete, name="post_delete"),
    
    # localhost:8000/blog/post/123/comment
    url(r'^post/(?P<post_id>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    # localhost:8000/blog/comment/123/delete
    url(r'^comment/(?P<comment_id>\d+)/delete/$', views.comment_delete, name='comment_delete'),

]

