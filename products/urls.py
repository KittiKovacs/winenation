from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('wines', views.all_wines, name='wines'),
    path('wines/<int:product_id>/', views.wine_details, name='wine_details'),
    path('subscriptions', views.all_subscriptions, name='subscriptions'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
