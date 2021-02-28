from django.shortcuts import render, redirect, \
 reverse, HttpResponse


# Create your views here.


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_wine_to_bag(request, wine_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if wine_id in list(bag.keys()):
        bag[wine_id] += quantity
    else:
        bag[wine_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def add_subscription_to_bag(request, subscription_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if subscription_id in list(bag.keys()):
        bag[subscription_id] += quantity
    else:
        bag[subscription_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_wine_in_bag(request, wine_id):

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    try:
        if quantity > 0:
            bag[wine_id] = quantity
        else:
            bag.pop(wine_id)

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        return HttpResponse(status=500)


def adjust_subscription_in_bag(request, subscription_id):

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    try:
        if quantity > 0:
            bag[subscription_id] = quantity
        else:
            bag.pop(subscription_id)

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        return HttpResponse(status=500)


def remove_wine_from_bag(request, wine_id):
    """Remove the item from the shopping bag"""
    bag = request.session.get('bag', {})

    try:
        bag.pop(wine_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


def remove_subscription_from_bag(request, subscription_id):
    """Remove the item from the shopping bag"""
    bag = request.session.get('bag', {})

    try:
        bag.pop(subscription_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)