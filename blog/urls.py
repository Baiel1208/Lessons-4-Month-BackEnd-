from collections import UserList
from django.urls import path
from blog import views
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.IndexListViews.as_view(), name="index-page"),

    path("contacts/", views.get_contacts, name="contacts-page"),

    path("about/", TemplateView.as_view(template_name="blog/about.html"), name="about-page"),

    path("post/<int:pk>", views.PostDetailViews.as_view(), name="post-detail"),

    path("post/update/<int:pk>", views.PostUpdateViews.as_view(), name="post-update"),

    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),

    path("post/create", views.PostCreateViews.as_view(), name="post-create"),

    path("api/posts/list", views.PostListAPIView.as_view(), name="post-list-api"),

    path("api/posts/<int:id>", views.PostDetailAPIView.as_view(),
    name="post-detail-api"),

    path("api/users/list", views.UsersListAPIView.as_view(), name="users-list-api"),

    path("api/users/<int:id>", views.UsersDetailAPIView.as_view(), name="users-detail-api"),

]