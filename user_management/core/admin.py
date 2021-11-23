from uuid import uuid4

from django.contrib import admin

from .models import User, Role
from .utils import generate_id

# Register your models here.



class UserInline(admin.StackedInline):
    model = User
    extra = 1
    using = 'user_management'


class UserAdmin(admin.ModelAdmin):
    using = 'user_management'
    list_display = ('name', 'email', 'role')


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['id'].initial = generate_id()
        form.base_fields['id'].disabled = True
        form.base_fields['id'].widget.attrs['style'] = "border: transparent"
        return form


admin.site.register(User, UserAdmin)


class RoleAdmin(admin.ModelAdmin):
    using = 'user_management'
    inlines = [UserInline]
    # prepopulated_fields = {'id': ('id',)}

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['id'].initial = generate_id()
        form.base_fields['id'].disabled = True
        form.base_fields['id'].widget.attrs['style'] = "border: transparent"
        return form


admin.site.register(Role, RoleAdmin)
