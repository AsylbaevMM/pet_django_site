from django.urls import path, re_path
from .views import PostList, PostDetail, UserPostList
from drf_spectacular.views import SpectacularAPIView


urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    re_path('^user/(?P<username>.+)/$', UserPostList.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]