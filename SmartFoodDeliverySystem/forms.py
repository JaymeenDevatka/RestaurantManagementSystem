from django import forms
from .models import FoodItem, Order

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['food_item', 'customer_name']

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
