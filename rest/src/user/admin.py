from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['pk','email']
    extra_kwargs = {
            'is_email_verified': {'read_only': True}
        }
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('name','phone_no',)}),
    )
    fieldsets = UserAdmin.fieldsets+(
        (None,{'fields':('name','phone_no','is_email_verified')}),
    )
admin.site.register(User,CustomUserAdmin)
