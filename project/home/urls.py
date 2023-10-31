from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
path("", views.index, name="index"),
path("login/", views.login_request, name="login"),
path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
path("about/", views.about, name="about"),
path("registro/", views.registro, name="registro"),
]

urlpatterns += staticfiles_urlpatterns()