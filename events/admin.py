from django.contrib import admin
from .models import Venue
from .models import Members
from .models import Event

# Register your models here.

admin.site.register(Venue)
admin.site.register(Members)
admin.site.register(Event)