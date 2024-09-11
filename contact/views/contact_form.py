from django.shortcuts import render

from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        context = {
            'forms': ContactForm(request.POST)
        }

        return render(request, 'contact/create.html', context)

    context = {
        'forms': ContactForm(request.POST)
    }

    return render(request, 'contact/create.html', context)
