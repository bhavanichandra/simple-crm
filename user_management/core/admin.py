from django.contrib import admin

from utility.core import generate_id
from .models import User, Role


# Register your models here.


class UserInline(admin.StackedInline):
    model = User
    extra = 1
    using = 'user_management'


class UserAdmin(admin.ModelAdmin):
    using = 'user_management'
    list_display = ('name', 'email', 'role')
    readonly_fields = ('id', 'created_at', 'updated_at')

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
