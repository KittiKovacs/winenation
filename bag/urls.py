from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<wine_id>/', views.add_wine_to_bag, name='add_wine_to_bag'),
    path('add/<subscription_id>/', views.add_subscription_to_bag,
         name='add_subscription_to_bag'),
]
