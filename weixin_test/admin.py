from django.contrib import admin

from .models import Patient, Result, Test1, Test2, Test3

admin.site.register(Patient)
admin.site.register(Result)
admin.site.register(Test1)
admin.site.register(Test2)
admin.site.register(Test3)