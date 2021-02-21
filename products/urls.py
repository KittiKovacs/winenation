from django.urls import path
from . import views

urlpatterns = [
    path('wines', views.all_wines, name='wines'),
    path('wines/<int:wine_id>', views.wine_details, name='wine_details'),
    path('events', views.all_events, name='events'),
    path('about', views.about, name='about'),
    path('subscriptions', views.all_subscriptions, name='subscriptions'),
]
