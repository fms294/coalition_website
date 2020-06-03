from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation')
    list_filter = ('categories','date_creation',)
    search_fields = ('date_creation', 'categories')

    class Meta:
        model = Post


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
