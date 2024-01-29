from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('users/', views.users_view, name='users_view'),
    path('orders/<int:user_id>', views.order_view, name='order_view'),
    path('products/<int:user_id>/<int:days>', views.product_view, name='product_view'),
    path('products/<int:product_id>/update', views.product_update, name='product_update'),
    path('products/<int:product_id>/upload', views.product_upload_image, name='product_upload_image'),

]
