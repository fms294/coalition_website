from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . forms import FeedbackForm
# Create your views here.


def index(request):
    return render  (request, 'index.html')


def about(request):
    return render  (request, 'aboutus.html')


def contact(request):
    return render (request, 'contact.html')

# def feedback(request):
#     if request.method == "POST":
#         form = FeedbackForm
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.INFO, "Feedback Submitted.")
#             return redirect("feedback")
#         else:
#             form = FeedbackForm()
#         return render(request, "pages/contact.html", {'form':form})