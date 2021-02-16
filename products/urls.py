from django.urls import path
from . import views

urlpatterns = [
    path('wines', views.all_wines, name='wines'),
    path('wines/<int:wine_id>', views.wine_details, name='wine_details'),
    path('events', views.all_events, name='events'),
    path('events/<int:event_id>', views.event_details, name='event_details'),
    path('subscriptions', views.all_subscriptions, name='subscriptions'),
    path('subscriptions/<int:subscription_id>', views.subscription_details,
         name='subscription_details'),
]
