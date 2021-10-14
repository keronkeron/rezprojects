from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'created_at', 'update_at', 'is_published', "category", "get_photo")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ('is_published', "category")
    fields = ("id", 'title', "content", 'is_published', "category", "get_photo")

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "-"

    get_photo.short_description = "photo"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'title')
    list_display_links = ("id", "title")
    search_fields = ("title",)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)