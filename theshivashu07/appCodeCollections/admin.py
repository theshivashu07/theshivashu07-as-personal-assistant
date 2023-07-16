from django.contrib import admin
# Register your models here.
from .models import DataStructures,Plateforms,ProgrammingLanguages

admin.site.register(DataStructures)
admin.site.register(Plateforms)
admin.site.register(ProgrammingLanguages)

