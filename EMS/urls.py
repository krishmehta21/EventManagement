from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
# EMS\urls.py

from myapp.views import loggedout

from myapp.views import create_profile

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='loggedout'), name='logout'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
    path('rsvp/<int:event_id>/', views.rsvp, name='rsvp'),
    path('profile/create/', views.create_profile, name='create_profile'),  # Updated path for create_profile
    path('loggedout/', loggedout, name='loggedout'),  # Define the URL pattern for loggedout

    # Remove the path for loggedout if not needed
]






# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)