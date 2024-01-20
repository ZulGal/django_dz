from django.shortcuts import render
from dz_1.models import User, Product,Order
import logging
from django.http import HttpResponse
import random

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




