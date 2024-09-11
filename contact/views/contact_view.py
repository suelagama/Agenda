from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title_page': 'Página Inicial'
    }
    return render(request, 'contact/index.html', context)


def search(request):
    search_contact = request.GET.get('q', '').strip()

    if search_contact == '':
        return redirect('contatcs:index')

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_contact) |
        Q(last_name__icontains=search_contact) |
        Q(phone__icontains=search_contact) |
        Q(email__icontains=search_contact)).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'tilte_page': 'Search'
    }
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    contact_name = f'{single_contact.first_name} {single_contact.last_name}'

    context = {
        'contact': single_contact,
        'tilte_page': contact_name
    }
    return render(request, 'contact/contact.html', context)
