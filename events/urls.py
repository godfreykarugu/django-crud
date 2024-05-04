from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.eventList, name='events'),
    path('venues/', views.venueList, name='venues'),
    # path('add_venue/', views.addvenue, name='add-venue'),
    # path('venue/', views.addVenue, name='venue'),
    path('venue/', views.add_event, name='venue'),
    path('show-venue/<int:venue_id>/', views.showVenue, name='show-venue'),
    path('search_venue/', views.search_venue, name='search-venue'),
     path('update-venue/<int:venue_id>/', views.update_venue, name='update-venue'),
     path('delete_event/<int:event_id>/', views.delete_event, name='delete-event'),

]