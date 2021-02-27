from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:wine_id>/', views.add_wine_to_bag, name='add_wine_to_bag'),
    path('add/<int:subscription_id>/', views.add_subscription_to_bag,
         name='add_subscription_to_bag'),
    path('adjust/<int:wine_id>/', views.adjust_wine_in_bag,
         name='adjust_wine_in_bag'),
    path('adjust/<int:subscription_id>/', views.adjust_subscription_in_bag,
         name='adjust_subscription_in_bag'),
    path('remove/<int:wine_id>/', views.remove_wine_from_bag, name='remove_wine_from_bag'),
    path('remove/<int:subscription_id>/', views.remove_subscription_from_bag, name='remove_subscription_from_bag'),
]
