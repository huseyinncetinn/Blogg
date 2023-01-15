from django.contrib import admin
from .models import *

class ProfilAdmin(admin.ModelAdmin):
    list_display = ( 'kullanici' , 'slug',)
    readonly_fields = ('slug',)


# Register your models here.

admin.site.register(Post)
admin.site.register(Yorum)
admin.site.register(Hesap)
admin.site.register(Profile, ProfilAdmin)
# admin.site.register(Likes)

