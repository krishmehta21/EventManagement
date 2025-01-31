# views.py in myapp

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Event
from .forms import LoginForm 
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

from .models import Profile, Attendee

# Import the LoginForm from forms.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404, redirect

from .models import Profile, Attendee


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Check if the profile exists for the logged-in user
                try:
                    profile = Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    # If profile doesn't exist, create one
                    profile = Profile.objects.create(user=user)
                return redirect('index')  # Redirect to the index page after successful login
            else:
                # Invalid login
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

# views.py in myapp
def profile(request):
    try:
        # Retrieve the profile for the current user
        profile = Profile.objects.get(user=request.user)
        
        try:
            # Retrieve the attendee details associated with the profile
            attendee = Attendee.objects.get(profile=profile)
        except Attendee.DoesNotExist:
            # Handle case where attendee details do not exist
            # You may want to redirect to a page to update attendee details
            return render(request, 'profile_error.html')  # Render an error template
        
        # Retrieve RSVP'd events for the user profile
        rsvp_events = Event.objects.filter(rsvps=request.user)
        
    except Profile.DoesNotExist:
        # Handle case where profile does not exist
        return redirect('create_profile')  # Redirect to profile creation page
    
    return render(request, 'profile.html', {'user_profile': profile, 'attendee': attendee, 'rsvp_events': rsvp_events})

def rsvp(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            event.rsvps.add(request.user)
            return redirect('event_detail', event_id=event_id)
        else:
            # Handle case where user is not authenticated
            pass
    # Handle other HTTP methods
    
@login_required
def create_profile(request):
    try:
        # Check if the profile already exists for the current user
        profile = Profile.objects.get(user=request.user)
        
        if request.method == 'POST':
            # If profile exists, update it with the submitted data
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                # Check if attendee exists for the profile
                attendee, created = Attendee.objects.get_or_create(profile=profile)
                return redirect('profile')
        else:
            # If profile exists, populate the form with existing profile data
            form = ProfileForm(instance=profile)
    except Profile.DoesNotExist:
        # If profile does not exist, create a new profile for the user
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                # Create an Attendee instance and link it to the user's profile
                attendee = Attendee(profile=profile)
                attendee.save()
                return redirect('profile')
        else:
            form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def loggedout(request):
    # Your view logic for logging out here
    return render(request, 'loggedout.html')  # Example template for logged out page