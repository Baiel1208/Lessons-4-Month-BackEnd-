from django.urls import path ,include
from users import views


urlpatterns = [
    path("users/", include("django.contrib.auth.urls")),
    path("user/register", views.RegisterViews.as_view(), name="register"),
    
]