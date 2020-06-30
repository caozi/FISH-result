from django.contrib import admin

from .models import Patient, Result, Test

admin.site.register(Patient)
admin.site.register(Result)
admin.site.register(Test)
