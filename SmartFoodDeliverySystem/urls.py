from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/', views.food_list, name='food_list'),
    path('foods/add/', views.add_food, name='add_food'),
    path('foods/update/<int:pk>/', views.update_food, name='update_food'),
    path('foods/delete/<int:pk>/', views.delete_food, name='delete_food'),

    # Order Views
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.place_order, name='place_order'),
    path('orders/status/<int:pk>/', views.update_order_status, name='update_order_status'),
]
