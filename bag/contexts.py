from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Wine, Subscription


def bag_contents(request):

    bag_items = []
    total_1 = 0
    total_2 = 0
    total = total_1 + total_2
    product_count = 0
    bag = request.session.get('bag', {})

    for wine_id, quantity in bag.items():
        wine = get_object_or_404(Wine, pk=wine_id)
        total_1 += quantity * wine.price
        product_count += quantity
        bag_items.append({
            'wine_id': wine_id,
            'quantity': quantity,
            'wine': wine,
        })

    for subscription_id, quantity in bag.items():
        subscription = get_object_or_404(Subscription, pk=subscription_id)
        total_2 += quantity*subscription.price
        product_count += quantity
        bag_items.append({
            'subscription_id': subscription_id,
            'quantity': quantity,
            'subscription': subscription,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(
                   settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total_1': total_1,
        'total_2': total_2,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
