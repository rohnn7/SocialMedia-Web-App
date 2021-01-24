from django.conf.urls import url
from . import views

app_name = "groups"

urlpatterns=[
    url(r'^$', views.ListGroups.as_view(), name='all'),
    url(r'^new/$', views.CreateGroup.as_view(), name='create'),
    #instead of grabbing the pk we grabbed the name of the group as slug to form a proper url
    url(r'^posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
    url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
]
