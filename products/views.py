from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Wine, Event, Subscription

# Create your views here.


def all_wines(request):
    """ A view to show all products, including sorting and search queries """

    wines = Wine.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('wines'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            wines = wines.filter(queries)

    context = {
        'wines': wines,
        'search_term': query,
    }

    return render(request, 'products/wines.html', context)


def wine_details(request, wine_id):

    wine = get_object_or_404(Wine, pk=wine_id)

    context = {
        'wine': wine,
    }

    return render(request, 'products/wine_details.html', context)


def all_events(request):
    """ A view to show all events, including sorting and search queries """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'products/events.html', context)


def event_details(request, event_id):

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'products/event_details.html', context)


def all_subscriptions(request):
    """ A view to show all events, including sorting and search queries """

    subscriptions = Subscription.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'products/subscriptions.html', context)


def why_subscribe(request):
    """ A view to show all events, including sorting and search queries """
    return render(request, 'info/why_subscribe.html')


def about(request):
    """ A view to show all events, including sorting and search queries """
    return render(request, 'info/about.html')
