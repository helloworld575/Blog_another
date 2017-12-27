from django.contrib import admin
from .models import ImageModel

class ImageAdmin(admin.ModelAdmin):
    list_display = ("title","user","pub")
    list_filter = ("title",)
admin.site.register(ImageModel,ImageAdmin)
# Register your models here.
