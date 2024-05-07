from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . models import Event
from . models import Venue
from .forms import AddVenueForm,AddEventForm

# Create your views here.

def home(request):
    return render(request, 'events/home.html')

def about(request):
    return render(request,'events/about.html')

def venueList(request):
    venue_list = Venue.objects.all()

    
    return render(request,'events/venue_list.html',{'venue_list':venue_list})

def showVenue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request,'events/venue.html',{'venue':venue})

# search venue

def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['searched'] 
        # searched=request.POST.get('searched')
        venues=Venue.objects.filter(name__contains=searched)

        return render(request,'events/search_venue.html',{'searched':searched,'venues':venues})
    else:
        return render(request,'events/search_venue.html')

def update_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    form=AddVenueForm(request.POST or None,instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venues')

    return render(request,'events/update_venue.html',{'venue':venue,'form':form})

def eventList(request):
    event_list = Event.objects.all()

    return render(request,'events/event_list.html',{'event_list':event_list})

# delete event

def delete_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('events')

def addVenue(request):
    submitted=False
    if request.method=='POST':
        form =AddVenueForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/venue?submitted=True')
    else:
        form = AddVenueForm()
        # if 'submitted' in request.GET:
        #     submitted = True
        if 'submitted' in request.GET:
               submitted = True
    return render(request,'events/addVenue.html',{'form':form,'submitted':submitted})

def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')  # Redirect to event list page
    else:
        form = AddEventForm()
    return render(request, 'events/add_event.html', {'form': form})

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form=AddEventForm(request.POST or None,instance=event)
    if request.method == 'POST':
         
        if form.is_valid():
            form.save()
            return redirect('events')
    
    return render(request, 'events/update_event.html', {'form': form})