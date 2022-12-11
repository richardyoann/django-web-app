import string

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Contact, Adresse, Ville


# Create your views here.
def liste_contacts(request, *args, **kwargs):
    # print (args, kwargs)
    # print (request)
    page = request.GET.get("page")
    filtre_page = request.GET.get("lettre")
    alphabet = string.ascii_uppercase
    # print(alphabet)
    contacts = Contact.objects.all().filter(nom__startswith=filtre_page).order_by('nom')
    paginator = Paginator(contacts, 12)
    try:
        contacts = paginator.page(page)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    context = {"contacts": contacts, "letters": alphabet,"filtre_lettre":filtre_page}
    return render(request, 'contacts/contact.html', context)


def edit_contact(request, id_contact, *args, **kwargs):
    contact = get_object_or_404(Contact, pk=id_contact)  # Contact.objects.get(pk=id_contact)
    adresse = Adresse.objects.get(pk=int(contact.adressepostaleid))
    ville = adresse.villeid
    print('Appel view edit_contact : \nLe contact souhaité est : ')
    print(contact)
    print("Appel view edit_contact : \nL'adresse du contact est : ")
    print(adresse)
    print('Appel view edit_contact : \nLa ville du contact est : ')
    print(ville)
    context = {'contact': contact, 'adresse': adresse, 'ville': ville}
    return render(request, 'contacts/edit_contact.html', context)
