from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegisterForm


# Create your views here.
def index(request):
    context={}
    return render(request, "main_app/home.html", context)


def register_user(request):
    # if this is a POST request we need to process the form data 
    if request.method == "POST":
        # Create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # Check whether it's valid:
        if form.is_valid():
            # process data in form.cleaned_data as required:
            form.save()
            
            return HttpResponse("Thanks")
        
    # if a GET (or any other mehtod) we'll create a blank form
    else:
        form = RegisterForm()
        
    context = {"form": form}
        
    return render(request, "main_app/register.html", context)