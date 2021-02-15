from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_details, name='product_details'),
    path('', views.all_events, name='events'),
    path('<event_id>', views.event_details, name='event_details'),
    path('', views.all_subscriptions, name='subscriptions'),
    path('<subscription_id>', views.subscription_details,
         name='subsciption_details'),
]
