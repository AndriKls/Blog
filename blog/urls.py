from . import views
from django.urls import path


urlpatterns = [
    path("", views.Starting_Page.as_view(), name="starting-page"),
    path("posts/", views.Posts.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.Post_Detail.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
]
