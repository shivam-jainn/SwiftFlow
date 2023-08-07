from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm,LogInForm,ProfilePicForm
from .models import SwiftUser,Ride
from django.contrib.auth.views import LoginView
from .backends import EmailBackend
from django.contrib.auth.hashers import make_password

def register_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            # Handle the form data here if needed
            return redirect('login_page')  # Redirect to the login page after successful registration.
        else:
            return HttpResponse(f"{form.errors}")
    else:
        form = SignUpForm()
    return render(request, 'registerform/register.html', {'form': form})


from django.contrib.auth import authenticate, login

def login_page(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"email: {email}, Password: {password}")

            # Use the custom authentication backend to authenticate the user
            user = authenticate(request, email=email, password=password)

            print("views : ", user)
            if user is not None:
                login(request, user)  # No need to specify backend here
                # Handle successful login here if needed
                return redirect('home_page')  # Redirect to the desired URL after successful login
            else:
                return HttpResponse("Invalid login credentials.")
        else:
            print("Form errors:", form.errors)  # Debug message: print form errors to the console
            return HttpResponse("Invalid form data.")
    else:
        form = LogInForm()
    return render(request, 'registerform/login.html', {'form': form})


def home_page(request):
    ridelist = Ride.objects.all()
    return render(request,'registerform/home.html',{'ridelist':ridelist})


from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):

    user = request.user

    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # Save the new image file to the user object
            user.profile_pic = request.FILES['profile_pic']
            user.save()
            # Redirect to the profile view after successful update
            return redirect(reverse('user_profile'))
        else:
            # Display error messages if the form is not valid
            messages.error(request, 'Please correct the errors below.')


    # Assuming the user is logged in, get the user information

    # Check if the user has uploaded a collegeID image
    collegeID_url = user.collegeID.url if user.collegeID and user.collegeID.url else None

      # Check if the user has uploaded profile picture
    profile_pic_url = user.profile_pic.url if user.profile_pic and user.profile_pic.url else None

    # Check if the user has uploaded license picture
    license_pic_url = user.license_pic.url if user.license_pic and user.license_pic.url else None

    return render(request, 'registerform/profile.html', {'user': user, 'collegeID_url': collegeID_url,'profile_pic_url': profile_pic_url, 'license_pic_url': license_pic_url})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfilePicForm
from django.contrib import messages
from django.urls import reverse

@login_required
def update_profile_pic(request):
    """Updates the profile picture of the logged-in user."""
    user = request.user

    if request.method == 'POST':
        # Get the form data and the new image file from the request
        form = ProfilePicForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # Save the new image file to the user object
            user.profile_pic = request.FILES['profile_pic']
            user.save()
            # Redirect to the profile view after successful update
            return redirect(reverse('user_profile'))
        else:
            # Display error messages if the form is not valid
            messages.error(request, 'Please correct the errors below.')
    else:
        # Display the form with the current profile picture
        form = ProfilePicForm(instance=user)

    # Render the template with the form and the user object
    return render(request, 'profilepic_update_form.html', {'form': form, 'user': user})
