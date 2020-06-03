from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ('categories','created_on',)
    search_fields = ('created_on', 'categories')

    class Meta:
        model = Post


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
