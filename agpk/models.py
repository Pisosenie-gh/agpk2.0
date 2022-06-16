from django.db import models
from django.contrib.auth.models import User



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
    status = models.CharField(choices =ROOM_STATUS,max_length = 15, verbose_name='Статус')
    roomnumber = models.IntegerField(verbose_name='Номер комнаты')
    floor = models.IntegerField(verbose_name='Этаж', default=0)
    capacity = models.IntegerField(verbose_name='Вместимость', default=0)

    def __str__(self):
        return str(self.roomnumber)

class Reservation(models.Model):
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE, verbose_name='Комната')
    guest = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name='Жилец')
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username


