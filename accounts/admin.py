from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'gender')

admin.site.register(get_user_model(), UserAdmin)