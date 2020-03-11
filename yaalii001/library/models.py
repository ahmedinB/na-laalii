from django.db import models

# Create your models here.
class bookdata(models.Model):
    book=models.FileField(upload_to='bookstore')
    bookname=models.TextField(max_length=100)
    description=models.TextField()
    bookimg=models.ImageField(upload_to="bookimg")
    def __str__(self):
        return self.bookname
class comment(models.Model):
    title=models.CharField(blank='true',max_length=250)
    detail=models.TextField()