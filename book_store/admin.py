from django.contrib import admin

from .models import Book, Category


class CustomBookAdmin(admin.ModelAdmin):
    model = Book
    fieldsets = (
        ('Owner', {
            'fields': ('title',)
        }),
        ('Book Info', {
            'fields': (
                'description',
                'category',
                'author',
                'image'
            )
        }),
    )
    list_display = ('title', 'author')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')


admin.site.register(Book, CustomBookAdmin)
admin.site.register(Category)
