from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Sonralar istifade edilmesi ucun CustomUser yazildi
class MyUser(AbstractUser):
	pass

# Rutbe modeli
class Rutbe(models.Model):
	class Meta:
		verbose_name="Rütbə"
		verbose_name_plural="Rütbələr"
	ad=models.CharField(verbose_name="Rütbə adı",max_length=100,null=True)
	sekil=models.ImageField("Şəkil",upload_to="main/uploads/rutbeler",null=True,blank=True)

	def __str__(self):
		return self.ad

# Qosun novu modeli
class QosunNovu(models.Model):
	class Meta:
		verbose_name="Qoşun növü"
		verbose_name_plural="Qoşun növləri"
	ad=models.CharField(verbose_name="Qoşun adı", max_length=100,null=True)
	sekil=models.ImageField("Şəkil",upload_to="main/uploads/qosun_novleri",null=True,blank=True)

	def __str__(self):
		return self.ad

class Medallar(models.Model):
	class Meta:
		verbose_name="Medal"
		verbose_name_plural="Medallar"
	ad=models.CharField(verbose_name="Medal adı",max_length=100,null=True)
	sekil=models.ImageField("Şəkil",upload_to="main/uploads/medallar",null=True,blank=True)

	def __str__(self):
		return f"{self.ad}"


# Person classi Sehidlerin melumatlarini ozunde saxlayir
class Person(models.Model):
	kisi="Kişi"
	qadin="Qadın"
	secim=[
		(kisi,"Kişi"),
		(qadin,"Qadın")
	]
	class Meta:
		verbose_name="Şəhid"
		verbose_name_plural="Şəhidlər"

	#Universal identifier
	id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

	# Şəxsi məlumatlar --------------
	ad=models.CharField(verbose_name="Adı",max_length=50,default="")
	soyad=models.CharField(verbose_name="Soyadı",max_length=50,default="")
	ata_adi=models.CharField(verbose_name="Ata adı",max_length=50,default="")
	leqeb=models.CharField(verbose_name="Ləqəbi",max_length=100,default="yoxdur.",blank=True)
	dogum_tarixi=models.DateField(verbose_name="Doğum tarixi")
	vefat_tarixi=models.DateField(verbose_name="Vəfat tarixi")
	dogum_yeri=models.CharField(verbose_name="Doğulduğu yer",max_length=255)
	vefat_yeri=models.CharField(verbose_name="Vəfat yeri", max_length=255)
	vetendasligi=models.CharField(verbose_name="Vətəndaşlığı",max_length=50)
	cinsiyeti=models.CharField(verbose_name="Cinsiyyəti seçin",max_length=5,default=kisi,choices=secim)
	sekil=models.ImageField("Şəkil",upload_to="main/uploads/%d/%m/%Y",null=True,blank=True,default="static/img/default-man.jpg")
	
	# Hərbi məlumatlar --------------
	qosun_novu=models.OneToOneField(QosunNovu,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Qoşun növü")
	mensubiyyeti=models.CharField(verbose_name="Mənsubiyyəti",max_length=100, default="Azərbaycan Ordusu")
	xidmet_illeri=models.CharField(verbose_name="Xidmət illəri",max_length=100)
	rutbe=models.ManyToManyField(Rutbe,verbose_name="Rütbə")
	medallar=models.ManyToManyField(Medallar,verbose_name="Medallar")

	def get_full_name(self):
		_ = ""
		if self.cinsiyeti==self.kisi:
			_ = "oğlu"
		else:
			_ = "qızı"
		return f"{self.ad} {self.ata_adi} {_} {self.soyad}"

	def __str__(self):
		_=""
		if self.cinsiyeti==self.kisi:
			_ = "oğlu"
		else:
			_ = "qızı"
		return f"{self.ad} {self.ata_adi} {_} {self.soyad}"