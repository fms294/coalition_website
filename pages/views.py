from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import FeedbackForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    if request.method == "POST":
        form_class = FeedbackForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            messages.add_message(request, messages.INFO, "Votre message a ete recu, MERCI.")
            return redirect('contact')
    else:
        form_class = FeedbackForm()
    return render(request, 'contact.html', {'form': form_class})


def donation(request):
    return render(request, 'donation.html')


def carriere(request):
    return render(request, 'carriere.html')

