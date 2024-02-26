from django.contrib import admin
from .models import FormModel


# Register your models here.
@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', ]
    ordering = ['first_name', ]
