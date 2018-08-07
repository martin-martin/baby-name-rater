from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rater.forms import RateNameForm


# Create your views here.
def signup_user(request):
    # only show the forms if the user is not logged in
    if request.user.is_authenticated:
        return redirect('/home')
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # first see whether all is good
            form.save()  # at this point the new user is created
            # now we want to log them in right away, for UX reasons
            # therefore we'll fetch username and pwd from the form
            username = form.cleaned_data.get('username')
            # ATTENTION: it's important to fetch 'password1' (which is
            # the original password) instead of just 'password', which
            # does not exist! However, .get() will not fail with an
            # exception if it doesn't find the key in the dictionary!
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/home')
    else:
        # if the user is not submitting, create an empty form
        # this runs the first time the user accesses the site
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    # only show the forms if the user is not logged in
    if request.user.is_authenticated:
        return redirect('/home')
    elif request.method == 'POST':
        # It's really important to remember to put `data=request.POST`
        # The AuthenticationForm works a little different than the other
        # forms, so the request is not its default first input...
        # messy - but that's how it is!
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def home(request):
    if request.method == 'POST':
        form = RateNameForm(request.POST)
    else:
        form = RateNameForm()
    return render(request, 'home.html', {'form': form})
