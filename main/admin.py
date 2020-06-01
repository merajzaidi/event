from django.contrib import admin
from .models import slider,postrequest,city , Shaiyar, contact, User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserAdminCreationForm, UserAdminChangeForm
User = get_user_model()
# Register your models here.
admin.site.register(slider)
#admin.site.register(postrequest)
admin.site.register(city)
#admin.site.register(Shaiyar)
admin.site.register(contact)

class ShaiyarAdmin(admin.StackedInline):
    model = Shaiyar

@admin.register(postrequest)
class PostAdmin(admin.ModelAdmin):
    inlines = [ShaiyarAdmin]

    class Meta:
       model = postrequest

@admin.register(Shaiyar)
class ShaiyarAdmin(admin.ModelAdmin):
    pass

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('email','superuser')
    list_filter = ('superuser',)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Personel info',{'fields':('full_name',)}),
        ('Permissions', {'fields':('superuser','staff','active','volunteer',)}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','password1','password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)