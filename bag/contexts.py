from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Wine, Subscription


def bag_contents(request):

    bag_items = []
    total1 = 0
    total2 = 0
    subtotal = total1 + total2
    product_count = 0
    bag = request.session.get('bag', {})

    for wine_id, quantity in bag.items():
        wine = get_object_or_404(Wine, pk=wine_id)
        total2 += quantity * wine.price
        product_count += quantity
        bag_items.append({
            'wine_id': wine_id,
            'quantity': quantity,
            'wine': wine,
        })

    for subscription_id, quantity in bag.items():
        subscription = get_object_or_404(Subscription, pk=subscription_id)
        total1 += quantity*subscription.price
        product_count += quantity
        bag_items.append({
            'subscription_id': subscription_id,
            'quantity': quantity,
            'subscription': subscription,
        })

    if subtotal < settings.FREE_DELIVERY_THRESHOLD:
        delivery = subtotal * Decimal(
                   settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - subtotal
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + subtotal

    context = {
        'bag_items': bag_items,
        'total1': total1,
        'total2': total2,
        'subtotal': subtotal,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
