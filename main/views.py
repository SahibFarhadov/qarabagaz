from django.shortcuts import render
from .models import *

def index(request):
	persons=Person.objects.all()
	context={
		"persons":persons
	}
	return render(request,"main/index.html",context)

def sehidler(request):
	persons=Person.objects.all()
	context={
		"persons":persons
	}
	return render(request,"main/sehidler.html",context)

def sehid(request,id):
	person = Person.objects.get(id=id)
	context={
		"person":person
	}
	return render(request,"main/sehid.html",context)
