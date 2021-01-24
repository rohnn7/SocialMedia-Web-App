from django.conf.urls import url
from posts import views
app_name = 'posts'

urlpatterns=[
    url(r'^$', views.PostList.as_view(), name='all'),
    url(r'new/$', views.CreatePost.as_view(), name='create'),
    url(r'by/(?P<username>[-\w]+)', views.UserPosts.as_view(template_name='posts/user_post_list.html'), name='for_user'),
    url(r'detail/posted/by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetail.as_view(template_name='posts/post_detail.html'), name='single'),
    url(r'delete/(?P<pk>\d+)/$',views.DeletePost.as_view(), name='delete'),
]
