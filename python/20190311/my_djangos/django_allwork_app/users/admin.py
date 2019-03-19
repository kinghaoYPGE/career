from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'is_admin', 'is_active', )
    list_filter = ('is_admin', 'is_active', )
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('first_name', )}),
        ('Permission', {'fields': ('is_admin', 'is_active', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    search_fields = ('username', 'email', )
    ordering = ('-date_modified', )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

