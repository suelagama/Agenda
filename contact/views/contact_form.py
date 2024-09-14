from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact

LINK_RENDER_CREATE = 'contact/create.html'
LINK_REVERSE_UPDATE = 'contact:update'


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        forms = ContactForm(request.POST, request.FILES)

        context = {
            'forms': forms,
            'form_action': form_action
        }

        if forms.is_valid():
            contact = forms.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contact registered successfully!')
            return redirect(LINK_REVERSE_UPDATE, contact_id=contact.pk)

        return render(request, LINK_RENDER_CREATE, context)

    context = {
        'forms': ContactForm(),
        'form_action': form_action
    }

    return render(request, LINK_RENDER_CREATE, context)


def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse(LINK_REVERSE_UPDATE, args=(contact_id,))

    if request.method == 'POST':
        forms = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'forms': forms,
            'form_action': form_action
        }

        if forms.is_valid():
            contact = forms.save()
            messages.success(request, 'Contact updated successfully!')
            return redirect(LINK_REVERSE_UPDATE, contact_id=contact.pk)

        return render(request, LINK_RENDER_CREATE, context)

    context = {
        'forms': ContactForm(instance=contact),
        'form_action': form_action
    }

    return render(request, LINK_RENDER_CREATE, context)


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    context = {
        'contact': contact,
        'confirmation': confirmation
    }

    return render(request, 'contact/contact.html', context)
