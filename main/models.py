from django.db import models
from django_resized import ResizedImageField
# Create your models here.


class Mahsulotlar(models.Model):
    rasm = ResizedImageField(size=[330, 440], upload_to='media/')
    sarlavha = models.CharField(max_length=120, null=True,blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha
    
class BizningMahsulot(models.Model):
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi


class Youtube(models.Model):
    link = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    

class AboutAwards(models.Model):
    rasm = models.ImageField(upload_to='media/')
    sarlavha = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha

class Xodimlar(models.Model):
    ismfamilya = models.CharField(max_length=200)
    kasbi = models.CharField(max_length=200)
    rasmi = models.ImageField(upload_to='media/')
    instagram = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    youtube = models.CharField(max_length=300)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ismfamilya
    
class ContactForm(models.Model):
    ismfamilya = models.CharField(max_length=200)
    pochta = models.EmailField(null=True,blank=True)
    telefon = models.CharField(max_length=20)
    murojaat_sababi = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.ismfamilya