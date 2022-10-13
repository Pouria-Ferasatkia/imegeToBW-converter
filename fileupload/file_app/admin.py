from django.contrib import admin
from .models import Video

@admin.register(Video)
class FileAdmin(admin.ModelAdmin):
    pass