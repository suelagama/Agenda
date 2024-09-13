
from django.contrib import messages
from django.shortcuts import redirect, render

from contact.forms import RegisterForm


def register(request):
    forms = RegisterForm()

    if request.method == 'POST':
        forms = RegisterForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, 'User registered successfully!')
            return redirect('contact:index')

    return render(request, 'contact/register.html', {'forms': forms})
