from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import login_request, CustomLogoutView, register_request, editar_request, editar_avatar_request

urlpatterns = [
    path('', login_request, name='Login'),
    path('login/', login_request, name='Login'),
    path('logout/', CustomLogoutView.as_view(), name='Logout'),
    path('register/', register_request, name='Registro'),
    path('editar/', editar_request, name='Editar'),
    path('avatar/', editar_avatar_request, name="Editar_avatar"),

    ]
