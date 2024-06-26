from django .forms import forms
from django .forms import ModelForm
from . models import Venue, Event


class AddEventForm(ModelForm):

    class Meta:
        model=Event
        fields = ('name','date','Venue','manager','description','attendees')

class AddVenueForm(ModelForm):

    class Meta:
        model=Venue
        fields = ('name','addres','zip_code','phone','web','email_address')