from django.contrib import admin
from .models import ArticleModel,ArticleColumn

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","create_pub")
    list_filter = ("create_pub","author")
    search_fields = ("title","body")
    raw_id_fields = ("author",)
    date_hierarchy = "create_pub"
    ordering = ["create_pub","author"]

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ("column","pub","user")
    list_filter = ("column",)

admin.site.register(ArticleColumn,ArticleColumnAdmin)
admin.site.register(ArticleModel,ArticleAdmin)
# Register your models here.
