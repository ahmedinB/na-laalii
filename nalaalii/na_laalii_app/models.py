from django.db import models
from datetime import datetime
from PIL import Image
class DEALER(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=200)
    password =models.CharField(max_length=50)
    keyword=models.CharField(max_length=350,blank=True)
    def __str__(self):
        return self.full_name
class pro(models.Model):
    logo=models.ImageField(upload_to="logo")
    bg1=models.ImageField(upload_to="bg1" , blank=True)
    bg2=models.ImageField(upload_to="bg2" , blank=True)

class feedback(models.Model):
    title=models.CharField(max_length=150)
    body=models.CharField(max_length=1000)

class mtrlinfo(models.Model):
    description=models.CharField(max_length=200)
    mapp_address = models.ImageField(upload_to='map_address' ,blank=True)
    cost = models.IntegerField()
    frontal_picture = models.ImageField(upload_to='frontal_picture')
    word_address = models.CharField(max_length=150)
    no_of_rooms = models.IntegerField()
    dealer=models.ForeignKey(DEALER,on_delete=models.CASCADE ,null=True)
    photo_from_inside =models.ImageField(upload_to='photo_from_inside')
    rooms_in_birdeye=models.ImageField(upload_to='rooms_in_birdeye')
    timestamp = models.DateTimeField( default=datetime.now , blank=True)

    def __str__(self):
        return self.description
