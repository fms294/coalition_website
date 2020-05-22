from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . forms import FeedbackForm
# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Feedback Submitted.")
            return redirect("feedback")
        else:
            form = FeedbackForm()
        return render(request, "pages/feedback.html", {'form':form})