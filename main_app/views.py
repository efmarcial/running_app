from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegisterForm

# Django Auth
from django.contrib.auth import authenticate, login, logout
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

def profile(request):
    
    # Auth in web request.
    if  request.user.is_authenticated:
        print("user is auth")
        # Get current user profile
    
    else:
        print('user not auth')
        return redirect("login/")
    
    context = {}
    
    return render(request, "main_app/profile.html", context)

# login view
def login_user(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            if user is not None:
                login(request, user)
                # redirect to a sucess page.
                return HttpResponse('profile')
            else:
                return HttpResponse('Invalid login error')
        except Exception as e:
            print(e)
    
    context = {}
        
    return render(request, "main_app/login.html", context)
        

def logout_view(request):
    logout(request)
    print('Logout successful')
    return HttpResponse("Logout successful")
    