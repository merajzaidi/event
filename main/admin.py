from django.contrib import admin
from .models import slider,postrequest,city , Shaiyar, contact
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