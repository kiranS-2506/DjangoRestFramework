from django.contrib import admin
from .models import student
class studentAdmin(admin.ModelAdmin):
    list_display = ['id','sno','sname','branch','saddr']
admin.site.register(student,studentAdmin)

# Register your models here.
