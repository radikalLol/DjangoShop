from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Profile, user
from .forms import UserEditForm

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


admin.site.register(Profile, ProfileAdmin)

class CustomUserAdmin(UserAdmin):
    form = UserEditForm
    model = user
    list_display = ['email', 'username', 'first_name', 'token']

admin.site.register(user, CustomUserAdmin)
