from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Модель данных о клиентах:
# - Определение полей для хранения персональных данных клиентов
#   (имя, фамилия, адрес, номер телефона, дата рождения, хобби, предыдущее место работы).

class ClientsInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField()
    hobby = models.CharField(max_length=200)
    last_work = models.CharField(max_length=200)

# - Учет предпочтений клиентов по продуктам(любимые категории, предпочтительные бренды).
class ClientsProducts(models.Model):
    client = models.ForeignKey(ClientsInfo, on_delete=models.CASCADE)
    categories = models.TextField()
    brands = models.TextField()