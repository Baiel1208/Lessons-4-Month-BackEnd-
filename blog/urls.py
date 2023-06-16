from django.urls import path
from blog import views


urlpatterns = [
    path("", views.index, name="index-page"),
    path("contacts/", views.get_contacts, name="contacts-page"),
    path("about/", views.get_about, name="about-page"),
    path("post/<str:pk>", views.get_post_detail, name="post-detail"),
# HW4
    path("post/update/<str:pk>", views.get_post_update, name="post-update"),
    path("post/delete/<str:pk>", views.get_post_delete, name="post-delete"),
]