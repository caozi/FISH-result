from django.contrib import admin

from .models import Patient, Result, Test, TestItem

admin.site.register(Patient)
admin.site.register(Result)
admin.site.register(Test)
admin.site.register(TestItem)