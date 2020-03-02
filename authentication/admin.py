from django.contrib import admin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
from . import models as authenticate_models
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('email', 'admin','staff')
    list_filter = (['admin','staff'])
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.register(authenticate_models.StudentRequests)

admin.site.register(authenticate_models.FacultyRequests)

admin.site.unregister(Group)