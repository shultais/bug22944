# -*- coding: utf-8 -*-
from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Book, BookAdmin)