from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Contact, Adresse, Ville


# Create your views here.
def liste_contacts(request, *args, **kwargs):
    contacts = Contact.objects.all().order_by('nom')
    context = {'contacts': contacts}
    return render(request, 'contact.html', context)

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
