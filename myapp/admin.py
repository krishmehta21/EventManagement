from django.contrib import admin
from .models import Event, Attendee, Venue, Category

admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Venue)
admin.site.register(Category)
