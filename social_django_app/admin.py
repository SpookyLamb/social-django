from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from social_django_app.models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

class TextPostAdmin(admin.ModelAdmin):
    pass

class ImagePostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(TextPost, TextPostAdmin)
admin.site.register(ImagePost, ImagePostAdmin)