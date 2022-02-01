from django.urls import path
from . import views
from home.views import setHome
from django.contrib.auth.views import LogoutView
from full_site import settings

urlpatterns = [
    path("", views.setHome, name="home"),
    path("/", views.setHome),
    path("login/", views.LoginView.as_view(), name="login"),
    path("registration/", views.Registration.as_view(), name="registration"),
    path(r'logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]
