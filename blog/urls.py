from django.urls import path
from blog import views


urlpatterns = [
    path("", views.index, name="index-page"),
    path("contacts/", views.get_contacts, name="contacts-page"),
    path("about/",views.get_about, name="about-page"),

]