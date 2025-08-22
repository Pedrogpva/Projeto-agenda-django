from django.shortcuts import get_object_or_404, redirect, render
from contact.models import Contact
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(request, 'contact/create.html', context)
    context = {
            'form': ContactForm()
        }
    print(request.method)
    return render(request, 'contact/create.html', context)
