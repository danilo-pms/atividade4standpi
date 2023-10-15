from django.urls import path
from .views import login_view as login, logout_view, create_user

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create_user/", create_user, name="create_user"),
    
]
