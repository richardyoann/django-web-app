from django.shortcuts import render
from django.http import HttpResponse
from contacts.models import Contact, Adresse, Ville 

# Create your views here.
def liste_contacts(request,*args, **kwargs):
    # print (args, kwargs)
    # print (request)
    contacts = Contact.objects.all().order_by('nom')
    context ={ 'contacts' : contacts }    
    return render(request, 'contact.html',context)
    

def edit_contact(request,id_contact, *args, **kwargs):
    # print (args, kwargs)
    # print (request)
    contact = Contact.objects.filter(contactid = int(id_contact)).select_related('Adresse').select_related('Ville')      
    context ={ 'contacts' : contact }    
    return render(request, 'edit_contact.html',context)
    # request, 'index.html', {"contacts":contacts})
    # return render(request, 'base.html', context = {"contacts":contacts})