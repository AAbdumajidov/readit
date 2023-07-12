from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact:index')
    ctx = {
        "form": form
    }
    return render(request, 'readit/contact.html', ctx)
