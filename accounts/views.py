from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from accounts.models import Avatar


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get("username")
            contrasenia = data.get("password")
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect("/app/mostrar_productos")
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    else:
        form = AuthenticationForm()

    contexto = {
        'form': form
    }
    return render(request, "accounts/login.html", contexto)


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        contexto = {

        }
        messages.success(request, '¡Has cerrado sesión con éxito!')
        return render(request, 'accounts/logout.html', contexto)


def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)


@login_required
def editar_request(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.save()
            return redirect("/app/mostrar_productos")

    form = UserUpdateForm(initial={"email": user.email, "first_name": user.first_name, "last_name": user.last_name})
    contexto = {
        "form": form
    }

    return render(request, "accounts/editar_usuario.html", contexto)


@login_required
def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.imagen = data['imagen']

            except:
                avatar = Avatar(
                    user=user,
                    imagen=data['imagen']

                )
            avatar.save()

        return redirect("/app/mostrar_productos")

    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)
