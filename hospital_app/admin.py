from django.contrib import admin
from .models import *   #เอามาหมดทุก class
# Register your models here.
admin.site.register(d_type)
admin.site.register(drug)