from django.db import models
from django.contrib.auth.models import User

class Hotels(models.Model):

    name = models.CharField(max_length=30,default="AGPK", verbose_name='Название')
    owner = models.CharField(max_length=20, verbose_name='Владелец')
    location = models.CharField(max_length=50, verbose_name='Метоположение')

    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 


    room_type = models.CharField(max_length=50,choices = ROOM_TYPE, verbose_name='Тип комнаты')
    capacity = models.IntegerField(verbose_name='Вместимость')
    price = models.IntegerField(verbose_name='Цена')
    size = models.IntegerField(verbose_name='Размер')
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE, verbose_name='Общежитие')
    status = models.CharField(choices =ROOM_STATUS,max_length = 15, verbose_name='Статус')
    roomnumber = models.IntegerField(verbose_name='Номер комнаты')
    floor = models.IntegerField(verbose_name='Этаж', default=0)
    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False, verbose_name='Вьезд')
    check_out = models.DateField(verbose_name='Выезд')
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE, verbose_name='Комната')
    guest = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name='Жилец')
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username


