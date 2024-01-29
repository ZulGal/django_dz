from django.shortcuts import render
from dz_1.models import User, Product,Order
import logging
from django.http import HttpResponse
import numpy as np
from  datetime import timedelta, datetime, timezone
from .forms import ProductUpdateForm
from django.core.files.storage import FileSystemStorage
from .forms import ProductUploadImageForm

logger = logging.getLogger(__name__)
def index (request):
    logger.info('index')
    html = """
    <h1>Привет, меня зовут Алекс</h1>
    <p>Это мой первый сайт на фреймворке Django<br/>Посмотрите на мой сайт.</p>
    """
    return HttpResponse(html)
def about (request):
    logger.info('about me')
    html = """
    <h3> Обо мне</h3>
    <p>Я изучал до этого: </p>
    <ul>
      <li>Python</li>
      <li>Flask</li>
      <li>FastApi</li>
      
    </ul>
    """
    return HttpResponse(html)

def users_view(request):
    users = User.objects.all()
    res_str = '<br>'.join([str(user) for user in users])
    return HttpResponse(res_str)

# def post_view(request,post_id):
#     post = Post.objects.get(id=post_id)
#     return render (request,template_name='dz_1/post.html', context={'post':post})

def order_view(request,user_id):
    user = User.objects.get(id=user_id)
    orders = Order.objects.filter(customer=user)

    dict_orders={}
    for order in orders:
        products=Product.objects.filter(order=order)
        list_products = []
        for product in products:
            list_products.append(product)
        dict_orders[order.id]=list_products
    context = {'user': user, 'dict_orders':dict_orders}
    return render (request,template_name='dz_1/order_view.html', context=context)

def product_view(request,user_id,days):
    user = User.objects.get(id=user_id)
    orders = Order.objects.filter(customer=user)
    dict_products = {}
    for order in orders:
        products=Product.objects.filter(order=order)
        for product in products:
            if  not product in dict_products:
                delta = datetime.now(timezone.utc) - order.date_ordered
                if delta.days <= days:
                    dict_products[product] = order.date_ordered

    keys = list(dict_products.keys())
    values = list(dict_products.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    context = {'user': user, 'dict_products':sorted_dict}
    return render (request,template_name='dz_1/product_view.html', context=context)

def product_update(request,product_id):
    message=''
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            message = 'Товар сохранён'
        else:
            message = 'Некорректные данные'
    else:
        form = ProductUpdateForm(instance=product)
    return render(request, 'dz_1/product_form.html', {'form':form, 'message': message})


def product_upload_image(request,product_id):
    message = ''
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductUploadImageForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            message = 'Фото загружено'
        else:
            message = 'Некорректные данные'
    else:
        form = ProductUploadImageForm(instance=product)
    return render(request, 'dz_1/product_upload_image.html', {'form': form, 'message': message})



