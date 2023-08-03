from django.urls import path
from . import views

urlpatterns=[
	path("",views.index),
	path("index",views.index,name="index"),
	path("sehidler",views.sehidler,name="sehidler"),
	path("sehid/<uuid:id>",views.sehid,name="sehid")
]