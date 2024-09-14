
from django.contrib import auth, messages  # type: ignore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    forms = RegisterForm()

    if request.method == 'POST':
        forms = RegisterForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, 'User registered successfully!')
            return redirect('contact:index')

    return render(request, 'contact/register.html', {'forms': forms})


@login_required(login_url='contact:login')
def user_update(request):
    forms = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(request, 'contact/user_update.html', {'forms': forms})

    forms = RegisterUpdateForm(request.POST, instance=request.user)

    if not forms.is_valid():
        return render(request, 'contact/user_update.html', {'forms': forms})

    forms.save()
    return redirect('contact:user_update')


def login_view(request):
    forms = AuthenticationForm(request)

    if request.method == 'POST':
        forms = AuthenticationForm(request, request.POST)

        if forms.is_valid():
            user = forms.get_user()
            auth.login(request, user)
            messages.success(request, 'User successfully logged in!')
            return redirect('contact:index')

        messages.error(request, 'Invalid username or password')

    return render(request, 'contact/login.html', {'forms': forms})


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)

    return redirect('contact:login')
