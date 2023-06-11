from django.urls import path
from blog import views


urlpatterns = [
    path("", views.index, name="index-page"),
    path("test-page/", views.test_page, name="test-page"),
# HW2
    path("conacts/", views.get_contacts, name="conacts-page"),
    path("about/",views.get_about, name="about-page"),

]