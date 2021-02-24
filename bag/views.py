from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_wine_to_bag(request, wine_id):
    """ Add a quantity of the specified product to the shopping bag """

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
    """ Add a quantity of the specified product to the shopping bag """

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
