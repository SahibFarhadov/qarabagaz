from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	pass

class Person(models.Model):
	# Şəxsi məlumatlar --------------
	ad_soyad=models.CharField(verbose_name="Ad və soyad",max_length=255)
	leqeb=models.CharField(verbose_name="Ləqəbi",max_length=100,default="yoxdur.",blank=True)
	dogum_tarixi=models.DateField(verbose_name="Doğum tarixi")
	vefat_tarixi=models.DateField(verbose_name="Vəfat tarixi")
	dogum_yeri=models.CharField(verbose_name="Doğulduğu yer",max_length=255)
	vefat_yeri=models.CharField(verbose_name="Vəfat yeri", max_length=255)
	vetendasligi=models.CharField(verbose_name="Vətəndaşlığı",max_length=50)
	
	# Hərbi məlumatlar --------------
	qosun_novu=models.CharField(verbose_name="Qoşun növü",max_length=100)
	mensubiyyeti=models.CharField(verbose_name="Mənsubiyyəti",max_length=100)
	xidmet_illeri=models.CharField(verbose_name="Xidmət illəri",max_length=100)


class Rutbe(models.Model):
	pass
