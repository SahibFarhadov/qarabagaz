from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(MyUser,UserAdmin)
admin.site.register(Person)
admin.site.register(Rutbe)
admin.site.register(QosunNovu)
admin.site.register(Medallar)