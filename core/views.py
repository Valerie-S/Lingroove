from django.shortcuts import render, redirect  # need to redirect user when they sign in
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "core/index.html")


# handle user sign up requests
def signup(request):
    # we know that the for has been clicked since it's a POST request
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # Check if username exists, if two passwords match. Django handles everything for us
        if form.is_valid():
            # create new user
            user = form.save()
            # Persist a user id and a backend in request. This way user doesn't have to reauthenticate on every request.
            login(request, user)
            messages.success(request, "Registration successful.")
            # redirect user to front page
            return redirect('index')
        messages.error(request, "Registration failed. Invalid information.")
    # If hasn't submitted form yet, create an empty instance of sign up form
    else:
        form = SignUpForm()
    # render sign up page and pass in the form as content
    return render(request, "core/signup.html", {'form': form})
