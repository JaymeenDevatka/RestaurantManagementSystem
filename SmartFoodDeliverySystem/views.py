from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem, Order, Restaurant
from .forms import FoodItemForm, OrderForm, OrderStatusForm

def home(request):
    return render(request, 'home.html')

def food_list(request):
    restaurant_id = request.GET.get('restaurant')
    if restaurant_id:
        food_items = FoodItem.objects.filter(restaurant__id=restaurant_id)
    else:
        food_items = FoodItem.objects.all()
    restaurants = Restaurant.objects.all()
    return render(request, 'food_list.html', {'food_items': food_items, 'restaurants': restaurants})

def add_food(request):
    form = FoodItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food_list')
    return render(request, 'food_form.html', {'form': form})

def update_food(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    form = FoodItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food_list')
    return render(request, 'food_form.html', {'form': form})

def delete_food(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    item.delete()
    return redirect('food_list')

def place_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'form': form})

def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderStatusForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order_status_form.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
