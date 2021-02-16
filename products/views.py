from django.shortcuts import render, get_object_or_404
from .models import Wine, Event, Subscription

# Create your views here.


def all_wines(request):
    """ A view to show all products, including sorting and search queries """

    wines = Wine.objects.all()

    context = {
        'wines': wines,
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


def subscription_details(request, subscription_id):

    subscription = get_object_or_404(Subscription, pk=subscription_id)

    context = {
        'subscription': subscription,
    }

    return render(request, 'products/subscription_details.html', context)
