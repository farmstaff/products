from django.db import models

# Create your models here.
class Products(models.Model):
    nomi = models.CharField(max_length=50)
    brendi = models.CharField(max_length=50)
    narxi = models.IntegerField()
    miqdori = models.IntegerField()


class Clients(models.Model):
    fio = models.CharField(max_length=80)
    dokon_nomi = models.CharField(max_length=50)
    telefon_raqami = models.IntegerField()
    manzil = models.CharField(max_length=80)


class Stats(models.Model):
    product = models.CharField(max_length=80)
    client = models.CharField(max_length=80)
    sana = models.DateField()
    miqdor = models.IntegerField()
    umumiy_summa = models.IntegerField()
    tolandi = models.IntegerField()
    nasiya = models.IntegerField()
    