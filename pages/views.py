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
            messages.add_message(request, messages.INFO, "Feedback Submitted.")
            return redirect('contact')
    else:
        form_class = FeedbackForm()
    return render(request, 'contact.html', {'form': form_class})
    # form_class = FeedbackForm
    #
    # return render(request, 'contact.html', {
    #     'form': form_class
    # })

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
