from django.urls import path ,include
from users import views
# from allauth.account.views import LoginView, LogoutView


urlpatterns = [
    path("users/", include("django.contrib.auth.urls")),
    path("user/register", views.RegisterViews.as_view(), name="register"),
    # path('accounts/', include('allauth.urls')),
]