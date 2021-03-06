from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('wines', views.all_wines, name='wines'),
    path('wines/<int:wine_id>', views.wine_details, name='wine_details'),
    path('subscriptions', views.all_subscriptions, name='subscriptions'),
]
