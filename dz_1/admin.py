from django.contrib import admin
from .models import User, Product,Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_registration']
    ordering = ['name']

    readonly_fields = ['date_registration']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity','date_added']
    ordering = ['quantity']
    list_filter = ['title','date_added']
    search_fields = ['title']
    search_help_text = 'Поиск по полю Наименование'

    readonly_fields = ['price', 'date_added']

    fieldsets = [
        (
            'Product',
            {
                'classes': ['wide'],
                'fields': ['title', 'price', 'quantity'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Описание ',
                'fields': ['description'],
            },
        ),

        (
            'Other',
            {
                'description': 'Прочая информация',
                'fields': ['date_added'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','total_price','date_ordered']
    ordering = ['date_ordered','customer']
    list_filter = ['products']

    readonly_fields = ['products','date_ordered']


admin.site.register(User,UserAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
