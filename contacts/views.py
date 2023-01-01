from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.views.generic import DetailView


# contact list view
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})

# Generic view for detail view
class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'

# contact create view
def create_contact(request):
    # form_class = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/create_contact.html', {'form': form})

# contact edit view
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form})

# contact delete
def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('list_contacts')