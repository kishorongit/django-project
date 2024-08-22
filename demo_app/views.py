from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TeacherForm
from .models import Teacher
# Create your views here.


def index_view(request):
    return render(request, "demo_app/index.html")


def teacher_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TeacherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # save valid and clean data
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeacherForm()
        return render(request, "demo_app/forms.html", {"form": form})
