from django.shortcuts import render, get_object_or_404
from .models import Product, Event, Subscription

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def all_events(request):
    """ A view to show all events, including sorting and search queries """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)


def event_details(request, event_id):

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_details.html', context)


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

    return render(request, 'subscriptions/subscription_details.html', context)
