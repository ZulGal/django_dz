from django import forms
from .models import Product

# Задание №6
# Доработаем задачу про клиентов, заказы и товары из  прошлого семинара.
# Создайте форму для редактирования товаров в базе данных.
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description','price','quantity']

# Домашнее задание
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.

class ProductUploadImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'quantity','image']

